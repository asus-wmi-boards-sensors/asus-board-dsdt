import string


# Valid variable or function name
ASL_VALID_NAME = string.ascii_letters + string.digits + "_"
# operation with parameter
OPERATION_WITH_PARAMETERS = [
    "Name",
    "OperationRegion",
    "External",
    "Alias",
    "Mutex",
    "Event",
    "Store",
    "Notify",
    "Release",
    "Return",
    "And",
    # Create*Field
    "CreateBitField",
    "CreateByteField",
    "CreateWordField",
    "CreateDWordField",
    "CreateQWordField",
    "CreateField",
]


def skip_empty_text(buf):
    buf = buf.lstrip()
    pos = 0
    while buf and buf[pos] in (string.whitespace + "/"):
        if buf[pos] in string.whitespace:
            pos += 1
        elif buf[pos:pos + 2] == "//":
            end_pos = buf.find("\n", pos + 2)
            if end_pos == -1:
                return ""
            else:
                pos = end_pos + 1
        elif buf[pos:pos + 2] == "/*":
            end_pos = buf.find("*/", pos + 2)
            if end_pos == -1:
                return ""
            else:
                pos = end_pos + 2
        else:
            break
    return buf[pos:]


def get_operator_name(buf):
    pos = 0
    buf_len = len(buf)
    # call of function defined inside scope
    if buf.startswith("\\"):
        pos += 1
        # call any func without path
        while pos < buf_len and buf[pos] in (ASL_VALID_NAME + "."):
            pos += 1
    # call any func without path
    else:
        while pos < buf_len and buf[pos] in ASL_VALID_NAME:
            pos += 1
    return buf[:pos], buf[pos:]


def select_open_close(buf):
    brakets = {
        "[": 0,
        "{": 0,
        "(": 0,
    }
    pos = 0
    str_len = len(buf)
    while pos < str_len:
        if buf[pos] in brakets:
            brakets[buf[pos]] += 1
            pos += 1
        elif buf[pos] == "\"":
            end_pos = buf.find("\"", pos + 1)
            if end_pos == -1:
                return buf.strip(), ""
            else:
                pos = end_pos
            pos += 1
        elif buf[pos] == "}":
            brakets["{"] -= 1
            pos += 1
        elif buf[pos] == "]":
            brakets["["] -= 1
            pos += 1
        elif buf[pos] == ")":
            brakets["("] -= 1
            pos += 1
        elif buf[pos:pos + 2] == "//":
            end_pos = buf.find("\n", pos + 2)
            if end_pos == -1:
                return buf[:pos], ""
            else:
                buf_beg = buf[:pos]
                buf_end = buf[end_pos + 1:]
                buf = buf_beg + buf_end
                str_len = len(buf)
        elif buf[pos:pos + 2] == "/*":
            end_pos = buf.find("*/", pos + 2)
            if end_pos == -1:
                return buf[:pos], ""
            else:
                buf_beg = buf[:pos]
                buf_end = buf[end_pos + 2:]
                buf = buf_beg + buf_end
                str_len = len(buf)
        else:
            pos += 1

        all_closed = True
        for ch in brakets:
            if brakets[ch] > 0:
                all_closed = False

        if all_closed:
            break

    return buf[:pos].strip(), buf[pos:]

def parse_block(buf, path=None):
    result = {}

    buf = skip_empty_text(buf)
    operator, buf = get_operator_name(buf)
    result["operator"] = operator
    result["path"] = path
    buf = skip_empty_text(buf)
    if operator in [
        "DefinitionBlock", "Scope", "Device", "PowerResource", "Processor",
        "If", "Else", "ElseIf", "ThermalZone"
    ]:
        # Else does not have parameters
        if operator not in ["Else"]:
            result["parameters"], buf = select_open_close(buf)
        # gen path
        if operator in ("Scope", "Device"):
            args = result["parameters"]
            if args[0] != "(" and args[-1] != ")":
                raise Exception(args)
            args = args[1:-1].strip()
            if args == "\\":
                sub_path = None
            elif args[0] == "\\" or not path:
                sub_path = [args.replace("\\", "")]
            else:
                sub_path = path + [args]
        else:
            sub_path = path
        # get content
        buf = skip_empty_text(buf)
        result["content"] = []
        if "{" == buf[0]:
            buf = buf[1:]
            buf = skip_empty_text(buf)
            while buf and buf[0] != "}":
                el, buf = parse_block(buf, path=sub_path)
                result["content"].append(el)
                buf = skip_empty_text(buf)
        if buf and "}" == buf[0]:
            buf = buf[1:]
    elif operator in ["Method", "Field", "IndexField", "BankField", "Package"]:
        result["parameters"], buf = select_open_close(buf)
        buf = skip_empty_text(buf)
        result["content"], buf = select_open_close(buf)
        buf = skip_empty_text(buf)
    elif operator in OPERATION_WITH_PARAMETERS:
        result["parameters"], buf = select_open_close(buf)
    # call function in scope
    elif operator.startswith("\\"):
        result["parameters"], buf = select_open_close(buf)
    elif (
        operator in ["Zero", "Noop"] or
        (operator.startswith("0x") and len(operator) == 10) # some raw command
    ):
        # noop
        pass
    else:
        raise Exception(operator + "<===>" + buf[:100] + "...")
    return result, buf


def cleanup_lines(content):
    content = content.strip()
    # remove caret back
    content = content.replace("\r", " ")
    # remove tab
    content = content.replace("\t", " ")
    # cleanup white space before others
    for char in (" ", "\n"):
        # remove multiple spaces
        while f" {char}" in content:
            content = content.replace(f" {char}", char)
    # empty after new line
    for char in (" ", "\n"):
        while f"\n{char}" in content:
            content = content.replace(f"\n{char}", "\n")
    return content.strip()


def parse_asl(buf):
    result = []
    while buf:
        parsed_block, buf = parse_block(buf)
        result.append(parsed_block)
    return result


# search element with same properties with strictly same values
# returns first match, or whole match list
def asl_has_operator_with_params(asl_struct, asl_dict, whole=False):
    result = []
    for el in asl_struct:
        for name in asl_dict:
            if el.get(name) != asl_dict[name]:
                break
        else:
            if whole:
                result.append(el)
            else:
                return [el]
    return result


def asl_get_operator_with_params(asl_struct, operator, params):
    for el in asl_struct:
        if (
            el.get("operator") == operator and
            isinstance(el.get("parameters"), str) and
            el.get("parameters", "").startswith(params)
        ):
            return el
    else:
        return None


# search element contains required element by default,
# or all elements match to required
def search_block_with_name_parameter(asl_struct, asl_dict, parent=True):
    results = []
    if isinstance(asl_struct, list):
        for el in asl_struct:
            res = search_block_with_name_parameter(el, asl_dict, parent)
            if res:
                results += res
    elif isinstance(asl_struct, dict):
        if "content" in asl_struct and isinstance(asl_struct["content"], list):
            el = asl_has_operator_with_params(asl_struct["content"], asl_dict, whole=not parent)
            if el:
                if parent:
                    results.append(asl_struct)
                else:
                    results += el
            # go deeper
            res = search_block_with_name_parameter(asl_struct["content"], asl_dict, parent)
            if res:
                results += res
    return results


def decode_buffer_uuid_by_name(content, name):
    result = []
    start_buffer = f"({name}, Buffer ("
    if not content.startswith(start_buffer):
        return result
    # search buffer values start
    start_wdg = content.find("{", len(start_buffer) + 1)
    if start_wdg == -1:
        return result
    # search buffer values end
    end_wdg = content.find("}", start_wdg + 1)
    if end_wdg == -1:
       end_wdg = len(content) + 1
    # get buffer
    wdg_content = content[start_wdg + 1:end_wdg - 1]
    # get left values
    content = content[end_wdg:]
    # remove whitespaces
    wdg_content = wdg_content.replace("\n", " ")
    while "  " in wdg_content:
        wdg_content = wdg_content.replace("  ", " ")
    wdg_content = wdg_content.strip()
    while ", " in wdg_content:
        wdg_content = wdg_content.replace(", ", ",")
    # combine values to single string
    values = []
    for hex_value in wdg_content.split(","):
        values.append(hex_value[2:4])
    values_combined = "".join(values)
    # convert string to uuid:method:flags
    while values_combined:
        uuid_str = []
        begin_uuid = ""
        tmp_uuid = values_combined[:16]
        while tmp_uuid:
            begin_uuid += tmp_uuid[-2:]
            tmp_uuid = tmp_uuid[:-2]
        end_uuid = values_combined[16:40]
        uuid_str.append(begin_uuid[8:16])
        uuid_str.append(begin_uuid[4:8])
        uuid_str.append(begin_uuid[0:4])
        uuid_str.append(end_uuid[0:4])
        uuid_str.append(end_uuid[4:16])
        result.append(
            f"{name}:{'-'.join(uuid_str)}:{end_uuid[16:20]}:{end_uuid[20:]}"
        )
        values_combined = values_combined[40:]

    return result
