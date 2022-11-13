#!/usr/bin/python3
import sys
import os

# Upstreamed ec
EC_BOARDS = [
    "PRIME X470-PRO",
    "PRIME X570-PRO",
    "ProArt X570-CREATOR WIFI",
    "Pro WS X570-ACE",
    "ROG CROSSHAIR VIII DARK HERO",
    "ROG CROSSHAIR VIII FORMULA",
    "ROG CROSSHAIR VIII HERO",
    "ROG CROSSHAIR VIII HERO (WI-FI)",
    "ROG MAXIMUS XI HERO",
    "ROG MAXIMUS XI HERO (WI-FI)",
    "ROG CROSSHAIR VIII IMPACT",
    "ROG STRIX B550-E GAMING",
    "ROG STRIX B550-I GAMING",
    "ROG STRIX X570-E GAMING",
    "ROG STRIX X570-E GAMING WIFI II",
    "ROG STRIX X570-F GAMING",
    "ROG STRIX X570-I GAMING",
    "ROG STRIX Z690-A GAMING WIFI D4",
    "ROG ZENITH II EXTREME",
]

# Upstreamed wmi
WMI_BOARDS = [
    "PRIME X399-A",
    "PRIME X470-PRO",
    "ROG CROSSHAIR VI EXTREME",
    "CROSSHAIR VI HERO",
    "ROG CROSSHAIR VI HERO (WI-FI AC)",
    "ROG CROSSHAIR VII HERO",
    "ROG CROSSHAIR VII HERO (WI-FI)",
    "ROG STRIX B450-E GAMING",
    "ROG STRIX B450-F GAMING",
    "ROG STRIX B450-F GAMING II",
    "ROG STRIX B450-I GAMING",
    "ROG STRIX X399-E GAMING",
    "ROG STRIX X470-F GAMING",
    "ROG STRIX X470-I GAMING",
    "ROG ZENITH EXTREME",
    "ROG ZENITH EXTREME ALPHA",
]

# Upstreamed nct6775
NCT6775_BOARDS = [
    "PRO H410T",
    "ProArt X570-CREATOR WIFI",
    "Pro B550M-C",
    "Pro WS X570-ACE",
    "PRIME B360-PLUS",
    "PRIME B460-PLUS",
    "PRIME B550-PLUS",
    "PRIME B550M-A",
    "PRIME B550M-A (WI-FI)",
    "PRIME H410M-R",
    "PRIME X570-P",
    "PRIME X570-PRO",
    "ROG CROSSHAIR VIII DARK HERO",
    "ROG CROSSHAIR VIII FORMULA",
    "ROG CROSSHAIR VIII HERO",
    "ROG CROSSHAIR VIII IMPACT",
    "ROG STRIX B550-A GAMING",
    "ROG STRIX B550-E GAMING",
    "ROG STRIX B550-F GAMING",
    "ROG STRIX B550-F GAMING (WI-FI)",
    "ROG STRIX B550-F GAMING WIFI II",
    "ROG STRIX B550-I GAMING",
    "ROG STRIX B550-XE GAMING (WI-FI)",
    "ROG STRIX X570-E GAMING",
    "ROG STRIX X570-E GAMING WIFI II",
    "ROG STRIX X570-F GAMING",
    "ROG STRIX X570-I GAMING",
    "ROG STRIX Z390-E GAMING",
    "ROG STRIX Z390-F GAMING",
    "ROG STRIX Z390-H GAMING",
    "ROG STRIX Z390-I GAMING",
    "ROG STRIX Z490-A GAMING",
    "ROG STRIX Z490-E GAMING",
    "ROG STRIX Z490-F GAMING",
    "ROG STRIX Z490-G GAMING",
    "ROG STRIX Z490-G GAMING (WI-FI)",
    "ROG STRIX Z490-H GAMING",
    "ROG STRIX Z490-I GAMING",
    "TUF GAMING B550M-PLUS",
    "TUF GAMING B550M-PLUS (WI-FI)",
    "TUF GAMING B550-PLUS",
    "TUF GAMING B550-PLUS WIFI II",
    "TUF GAMING B550-PRO",
    "TUF GAMING X570-PLUS",
    "TUF GAMING X570-PLUS (WI-FI)",
    "TUF GAMING X570-PRO (WI-FI)",
    "TUF GAMING Z490-PLUS",
    "TUF GAMING Z490-PLUS (WI-FI)",
]

# Bios dump has diffrent name to board name
BOARDNAME_CONVERT = {
    "ROG STRIX X670E-I GAMING (WI-FI)": "ROG STRIX X670E-I GAMING WIFI",
    "PRO B550M-C-SI": "Pro B550M-C",
    "PRO H410T-SI": "PRO H410T",
    "PROART Z790-CREATOR-WIFI": "ProArt Z790-CREATOR WIFI",
    "PROART Z690-CREATOR-WIFI": "ProArt Z690-CREATOR WIFI",
    "PROART B660-CREATOR-D4": "ProArt B660-CREATOR D4",
    "PROART X670E-CREATOR-WIFI": "ProArt X670E-CREATOR WIFI",
    "PROART B550-CREATOR": "ProArt B550-CREATOR",
    "PROART X570-CREATOR-WIFI": "ProArt X570-CREATOR WIFI",
    "PROART Z490-CREATOR-10G": "ProArt Z490-CREATOR 10G",
    "ROG CROSSHAIR VI HERO WIFI AC": "ROG CROSSHAIR VI HERO (WI-FI AC)",
}

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
        if len(board_group[3]) == 1 or board_group[3].upper() == "PLUS":
            board_group = [
                board_group[0], board_group[1],
                f"{board_group[2]}-{board_group[3]}"
            ] + board_group[4:]
        # create name
        board_name = f"{board_group[0]} {board_group[1]} "
        board_name += " ".join(board_group[2:])
    elif board_group[0].upper() in ("PRO", "PRIME", "PROART"):
        # create name
        board_name = f"{board_group[0]} "
        board_name += "-".join(board_group[1:])
    elif board_group[0].upper() in ("MAXIMUS", "TUF", "CROSSHAIR"):
        # create name
        board_name = f"{board_group[0]} "
        board_name += " ".join(board_group[1:])
    else:
        board_name = "-".join(board_group)
    board_name = board_name.replace("_", " ")

    # conver board names
    if board_name.upper() in BOARDNAME_CONVERT:
        return BOARDNAME_CONVERT[board_name.upper()]
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


def add_board(board_name, asus_wmi, asus_nct6775, asus_ec):
    if board_name not in table:
        table[board_name] = []
    board_desc = (
        f"| {board_name}{' ' * (33 - len(board_name))}"
        f"| {asus_wmi}{' ' * (17 - len(asus_wmi)) }"
        f"| {asus_nct6775}{' ' * (8 - len(asus_nct6775))}"
        f"| {asus_ec}{' ' * (15 - len(asus_ec))} "
        f"|"
    )
    if board_desc not in table[board_name]:
        table[board_name].append(board_desc)


if __name__ == "__main__":
    current_dir = "."
    table = {}

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
                with open(f"{dirname}/{filename}", "br") as f:
                    content = f.read().decode("utf8")

                    asus_wmi = "N"
                    asus_ec = "N"
                    asus_nct6775 = "N"
                    if check_entrypoint(content):
                        if check_port(content):
                            if check_nct6775(content):
                                # already upstreamed
                                if board_name in NCT6775_BOARDS:
                                    asus_nct6775 = "Y"
                                else:
                                    asus_nct6775 = "U"
                            elif board_name in NCT6775_BOARDS:
                                asus_nct6775 = "?"
                            # Check ec
                            if check_ec(content):
                                if board_name in EC_BOARDS:
                                    asus_ec = "Y"
                                else:
                                    asus_ec = "U"
                            elif board_name in EC_BOARDS:
                                asus_ec = "?"
                            # Check wmi
                            if check_wmi(content):
                                if board_name in WMI_BOARDS:
                                    asus_wmi = "Y"
                                else:
                                    asus_wmi = "U"
                            elif board_name in WMI_BOARDS:
                                asus_wmi = "?"
                    # Workaround needed
                    if asus_nct6775 == "N" and check_custom_port(content):
                            asus_nct6775 = "P"
                print (f"Board: {board_name}")
                print (f"\tVersion: {board_version}")
                print (f"\tRevision: {board_hash}")
                print (f"\tProducer: {board_producer}")
                add_board(board_name, asus_wmi, asus_nct6775, asus_ec)

    for board_name in sorted(NCT6775_BOARDS + WMI_BOARDS + EC_BOARDS):
        # Just skip existed boards
        if board_name in table:
            continue
        add_board(
            board_name=board_name,
            asus_wmi="Y" if board_name in WMI_BOARDS else "N",
            asus_nct6775="Y" if board_name in NCT6775_BOARDS else "N",
            asus_ec="Y" if board_name in EC_BOARDS else "N"
        )

    print ("| board                            | asus_wmi_sensors | nct6777 | asus_ec_sensors |")
    for key in sorted(table.keys()):
        print ("\n".join(sorted(table[key])))
