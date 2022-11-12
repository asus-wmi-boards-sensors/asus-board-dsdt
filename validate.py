import sys
import os


def gen_board_name(board_group):
    if board_group[0] == "ROG" and board_group[1] == "STRIX":
        # fix WIFI name
        if board_group[-1].upper() == "WIFI":
            board_group[-1] = "(WI-FI)"
        # create name
        board_name = f"{board_group[0]} {board_group[1]} "
        board_name += f"{board_group[2]}-{board_group[3]} "
        board_name += " ".join(board_group[4:])
    elif board_group[0] == "ROG" and board_group[1] in ("CROSSHAIR", "MAXIMUS"):
        # fix WIFI name
        if board_group[-1].upper() == "WIFI":
            board_group[-1] = "(WI-FI)"
        # create name
        board_name = f"{board_group[0]} {board_group[1]} "
        board_name += " ".join(board_group[2:])
    elif board_group[0] == "TUF" and board_group[1] == "GAMING":
        # fix WIFI name
        if board_group[-1].upper() == "WIFI":
            board_group[-1] = "(WI-FI)"
        if len(board_group[3]) == 1:
            board_group = [
                board_group[0], board_group[1],
                f"{board_group[2]}-{board_group[3]}"
            ] + board_group[4:]
        # create name
        board_name = f"{board_group[0]} {board_group[1]} "
        board_name += " ".join(board_group[2:])
    elif board_group[0].upper() in ("PRO", "PRIME"):
        # create name
        board_name = f"{board_group[0]} "
        board_name += "-".join(board_group[1:])
    else:
        board_name = "-".join(board_group)
    board_name = board_name.replace("_", " ")
    return board_name


def check_entrypoint(content):
    if "/* 0000 */  0xD0, 0x5E, 0x84, 0x97, 0x6D, 0x4E, 0xDE, 0x11," not in content:
        return False
    if "/* 0008 */  0x8A, 0x39, 0x08, 0x00, 0x20, 0x0C, 0x9A, 0x66," not in content:
        return False
    return True


def check_port(content):
    if "Name (IOHW, 0x0290)" not in content:
        return False
    if ", SystemIO, IOHW, 0x0A)" not in content:
        return False
    return True

def cleanup_lines(content):
    while "\r" in content:
        content = content.replace("\r", " ")
    while "  " in content:
        content = content.replace("  ", " ")
    return content

def check_custom_port(content):
    for line in content.split("\n"):
        if ", 0x0290)" in line and "Name (" in line:
            return True
    return False


def check_method(content, method):
    if f"Method ({method}, 1, Serialized)" not in content:
        return False
    content = cleanup_lines(content)
    if f"Method ({method}, 1, Serialized)\n {{\n Return (Ones)\n }}\n" in content:
        return False
    return True


def check_wmi(content):
    if "Case (0x52574543)" not in content:
        return False
    if "Case (0x51574543)" not in content:
        return False
    if "Case (0x50574543)" not in content:
        return False
    if "Case (0x50574572)" not in content:
        return False
    if "Case (0x50574574)" not in content:
        return False
    if not check_method(content, "RSEN"):
        return False
    if not check_method(content, "GNAM"):
        return False
    if not check_method(content, "GNUM"):
        return False
    if not check_method(content, "UPSB"):
        return False
    if not check_method(content, "GVER"):
        return False
    return True


def check_ec(content):
    if "Case (0x42524543)" not in content:
        return False
    if not check_method(content, "BREC"):
        return False
    return True


def check_nct6775(content):
    if "Case (0x5253494F)" not in content:
        return False
    if "Case (0x5753494F)" not in content:
        return False
    if "Case (0x5248574D)" not in content:
        return False
    if "Case (0x5748574D)" not in content:
        return False
    if not check_method(content, "RSIO"):
        return False
    if not check_method(content, "WSIO"):
        return False
    if not check_method(content, "RHWM"):
        return False
    if not check_method(content, "WHWM"):
        return False
    return True


if __name__ == "__main__":
    current_dir = "."
    table = []

    if len(sys.argv) > 1:
        current_dir = sys.argv[1]

    for dirname, _, filenames in os.walk(current_dir):
        # print path to all filenames.
        for filename in filenames:
            if filename.endswith('.dsl'):
                file_parts = filename.split(".")
                if len(file_parts) != 3:
                    print (f"Can't parse filename: '{dirname}/{filename}'")
                board_group = file_parts[0].split("-")
                board_hash = file_parts[1]
                board_version = ""
                # check bios version
                if board_group[-1].isdigit():
                    board_version = int(board_group[-1])
                    board_group = board_group[:-1]
                # check board producer
                board_producer = ""
                if board_group[-1].upper() in ("ASUS"):
                    board_producer = board_group[-1].upper()
                    board_group = board_group[:-1]
                board_name = gen_board_name(board_group)
                with open(filename, "br") as f:
                    content = f.read().decode("utf8")

                    asus_wmi = "N"
                    asus_ec = "N"
                    asus_nct6775 = "N"
                    if check_entrypoint(content):
                        if check_port(content):
                            if check_nct6775(content):
                                asus_nct6775 = "Y"
                            if check_ec(content):
                                asus_ec = "Y"
                            if check_wmi(content):
                                asus_wmi = "Y"
                    # Workarount needed
                    if asus_nct6775 == "N" and check_custom_port(content):
                            asus_nct6775 = "P"
                print (f"Board: {board_name}, Version: {board_version} Revision: {board_hash}")
                table.append(
                    f"| {board_name} {' ' * (32 - len(board_name))} "
                    f"| {asus_wmi}{' ' * 3} "
                    f"| {asus_nct6775}{' ' * 3} "
                    f"| {asus_ec}{' ' * 3} "
                    f"| {board_hash} "
                    f"| {board_producer}{' ' * (4 - len(board_producer))} |"
                )

    print ("\n".join(sorted(table)))
