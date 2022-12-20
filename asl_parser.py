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
    while buf[pos] in ASL_VALID_NAME:
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


def parse_block(buf):
    result = {}

    buf = skip_empty_text(buf)
    operator, buf = get_operator_name(buf)
    result["operator"] = operator
    buf = skip_empty_text(buf)
    if operator in [
        "DefinitionBlock", "Scope", "Device", "PowerResource", "Processor",
        "If", "Else", "ElseIf", "ThermalZone"
    ]:
        if operator not in ["Else"]:
            result["parameters"], buf = select_open_close(buf)
        buf = skip_empty_text(buf)
        result["content"] = []
        if "{" == buf[0]:
            buf = buf[1:]
            buf = skip_empty_text(buf)
            while buf and buf[0] != "}":
                el, buf = parse_block(buf)
                result["content"].append(el)
                buf = skip_empty_text(buf)
        if buf and "}" == buf[0]:
            buf = buf[1:]
    elif operator in ["Method", "Field", "IndexField"]:
        result["parameters"], buf = select_open_close(buf)
        buf = skip_empty_text(buf)
        result["content"], buf = select_open_close(buf)
        buf = skip_empty_text(buf)
    elif operator in OPERATION_WITH_PARAMETERS:
        result["parameters"], buf = select_open_close(buf)
    elif operator in ["Zero"]:
        # noop
        pass
    # TODO: hack and fix
    elif buf[0] == "=":
        result["operator"] = "_SET_"
        line_size = buf.find("\n", 1)
        if line_size == -1:
            line_size = len(line_size)
        result["parameters"] = (operator, buf[:line_size + 1].strip())
        buf = buf[line_size + 1:].strip()
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
