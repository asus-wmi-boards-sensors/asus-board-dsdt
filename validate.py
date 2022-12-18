#!/usr/bin/python3
import sys
import os
import json


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

# Upstreamed gigabyte
GIGABYTE_BOARDS = [
    "B450M DS3H-CF",
    "B450M S2H V2",
    "B550 AORUS ELITE AX V2",
    "B550 AORUS ELITE",
    "B550 AORUS ELITE V2",
    "B550 GAMING X V2",
    "B550I AORUS PRO AX",
    "B550M AORUS PRO-P",
    "B550M DS3H",
    "B660 GAMING X DDR4",
    "B660I AORUS PRO DDR4",
    "Z390 I AORUS PRO WIFI-CF",
    "Z490 AORUS ELITE AC",
    "X570 AORUS ELITE",
    "X570 AORUS ELITE WIFI",
    "X570 GAMING X",
    "X570 I AORUS PRO WIFI",
    "X570 UD",
    "Z690M AORUS ELITE AX DDR4",
]

# Upstreamed nct6775 series
NCT6775_SERIES = [
    "ProArt B550",
    "ProArt X570",
    "ProArt Z490",
    "Pro B550",
    "Pro WS X570",
    "PRIME B360",
    "PRIME B460",
    "PRIME B550",
    "PRIME H410",
    "PRIME X570",
    "ROG CROSSHAIR VIII",
    "ROG STRIX B550",
    "ROG STRIX X570",
    "ROG STRIX Z390",
    "ROG STRIX Z490",
    "TUF GAMING B550",
    "TUF GAMING X570",
    "TUF GAMING Z490",
]

# Bios dump has diffrent name to board name
BOARDNAME_CONVERT = {
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
    "Z490-GUNDAM-WIFI": "Z490-GUNDAM (WI-FI)",
    "TUF GAMING Z590-PLUS (WI-FI)": "TUF GAMING Z590-PLUS WIFI",
    "TUF GAMING X570-PRO WIFI SI": "TUF GAMING X570-PRO (WI-FI)",
    "PRIME B450M-GAMING BR SI": "PRIME B450M-GAMING/BR",
}


# mutex names from kernel source
ASUS_NCT6775_MUTEX = {
    "\_SB.PC00.LPCB.SIO1.MUT0": [
        "ProArt B660-CREATOR D4", # "ASUSTeK Computer INC."
        "ProArt Z790-CREATOR WIFI", # "ASUSTeK Computer INC."
    ],
    "\_SB.PCI0.LPCB.SIO1.MUT0": [
        "PRIME H410M", # "ASUSTeK Computer INC."
    ],
    "\\_SB_.PCI0.LPCB.SIO1.MUT0": [
        "P8Z68-V LX", # "ASUSTeK Computer INC."
        "MAXIMUS VII HERO", # "ASUSTeK COMPUTER INC."
        "P8H67", # "ASUSTeK COMPUTER INC."
        "ROG MAXIMUS X HERO", # "ASUSTeK COMPUTER INC."
        "ROG STRIX Z370-H GAMING", # "ASUSTeK COMPUTER INC."
        "Z170-DELUXE", # "ASUSTeK COMPUTER INC."
        "Z170M-PLUS", # "ASUSTeK COMPUTER INC."
    ],
    "\\_SB_.PCI0.LPC0.SIO1.MUT0": [
        "X99-E WS/USB 3.1", # "ASUSTeK COMPUTER INC."
    ],
    "\\_SB.PCI0.SBRG.SIO1.MUT0": [
        "PRIME X370-PRO", # "ASUSTeK COMPUTER INC."
        "PRIME X470-PRO", # "ASUSTeK COMPUTER INC."
        "PRIME X399-A", # "ASUSTeK COMPUTER INC."
        "PRIME B450-PLUS", # "ASUSTeK COMPUTER INC." Need to recheck
        "PRIME B450M-GAMING", # "ASUSTeK COMPUTER INC."
        "PRIME Z270-A", # "ASUSTeK COMPUTER INC."
        "PRIME Z370-A", # "ASUSTeK COMPUTER INC."
        "ROG CROSSHAIR VI Hero", # "ASUSTeK COMPUTER INC."
        "ROG STRIX X399-E GAMING", # "ASUSTeK COMPUTER INC."
        "ROG STRIX B350-F GAMING", # "ASUSTeK COMPUTER INC."
        "ROG STRIX B450-F GAMING", # "ASUSTeK COMPUTER INC."
        "TUF B450 PLUS GAMING", # "ASUSTeK COMPUTER INC."
    ]
}

# mutex names from kernel source
ASUS_EC_MUTEX = {
    "\\AMW0.ASMX": [
        "ProArt X570-CREATOR WIFI", # "ASUSTeK COMPUTER INC."
        "Pro WS X570-ACE", # "ASUSTeK COMPUTER INC."
        "PRIME X570-PRO", # "ASUSTeK COMPUTER INC."
        "ROG CROSSHAIR VIII DARK HERO", # "ASUSTeK COMPUTER INC."
        "ROG CROSSHAIR VIII FORMULA", # "ASUSTeK COMPUTER INC."
        "ROG CROSSHAIR VIII HERO", # "ASUSTeK COMPUTER INC."
        "ROG CROSSHAIR VIII HERO (WI-FI)", # "ASUSTeK COMPUTER INC."
        "ROG CROSSHAIR VIII IMPACT", # "ASUSTeK COMPUTER INC."
        "ROG MAXIMUS XI HERO", # "ASUSTeK COMPUTER INC."
        "ROG MAXIMUS XI HERO (WI-FI)", # "ASUSTeK COMPUTER INC."
        "ROG STRIX B550-E GAMING", # "ASUSTeK COMPUTER INC."
        "ROG STRIX B550-I GAMING", # "ASUSTeK COMPUTER INC."
        "ROG STRIX X570-E GAMING", # "ASUSTeK COMPUTER INC."
        "ROG STRIX X570-E GAMING WIFI II", # "ASUSTeK COMPUTER INC."
        "ROG STRIX X570-F GAMING", # "ASUSTeK COMPUTER INC."
        "ROG STRIX X570-I GAMING", # "ASUSTeK COMPUTER INC."
    ],
    "\\RMTW.ASMX": [
        "ROG STRIX Z690-A GAMING WIFI D4", # "ASUSTeK COMPUTER INC."
    ],
    "\\_SB_.PCI0.SBRG.SIO1.MUT0": [
        "ROG ZENITH II EXTREME", # "ASUSTeK COMPUTER INC."
    ]
}

KNOWN_GOOD_IMPLEMENTATION = {
    "B550": """
        Device (AMW0)
        {
            Name (_HID, EisaId ("PNP0C14") )
            Name (_UID, "ASUSWMI")
            Name (_WDG, Buffer (0x50)
            {
                0xD0, 0x5E, 0x84, 0x97, 0x6D, 0x4E, 0xDE, 0x11,
                0x8A, 0x39, 0x08, 0x00, 0x20, 0x0C, 0x9A, 0x66,
                0x42, 0x43, 0x01, 0x02, 0xA0, 0x47, 0x67, 0x46,
                0xEC, 0x70, 0xDE, 0x11, 0x8A, 0x39, 0x08, 0x00,
                0x20, 0x0C, 0x9A, 0x66, 0x42, 0x44, 0x01, 0x02,
                0x72, 0x0F, 0xBC, 0xAB, 0xA1, 0x8E, 0xD1, 0x11,
                0x00, 0xA0, 0xC9, 0x06, 0x29, 0x10, 0x00, 0x00,
                0xD2, 0x00, 0x01, 0x08, 0x21, 0x12, 0x90, 0x05,
                0x66, 0xD5, 0xD1, 0x11, 0xB2, 0xF0, 0x00, 0xA0,
                0xC9, 0x06, 0x29, 0x10, 0x4D, 0x4F, 0x01, 0x00
            })
    """,
    "B650": """
        Device (RMTW)
        {
            Name (_HID, EisaId ("PNP0C14") )
            Name (_UID, "AsusMbSwInterface")
            Name (_WDG, Buffer (0x50)
            {
                0xD0, 0x5E, 0x84, 0x97, 0x6D, 0x4E, 0xDE, 0x11,
                0x8A, 0x39, 0x08, 0x00, 0x20, 0x0C, 0x9A, 0x66,
                0x42, 0x43, 0x01, 0x02, 0x15, 0xB1, 0x2B, 0xB8,
                0xAE, 0x43, 0x35, 0x4B, 0xB7, 0x9D, 0xBD, 0x64,
                0x16, 0xAB, 0xC3, 0x81, 0x42, 0x43, 0x01, 0x02,
                0x72, 0x0F, 0xBC, 0xAB, 0xA1, 0x8E, 0xD1, 0x11,
                0x00, 0xA0, 0xC9, 0x06, 0x29, 0x10, 0x00, 0x00,
                0xD2, 0x00, 0x01, 0x08, 0x21, 0x12, 0x90, 0x05,
                0x66, 0xD5, 0xD1, 0x11, 0xB2, 0xF0, 0x00, 0xA0,
                0xC9, 0x06, 0x29, 0x10, 0x4D, 0x4F, 0x01, 0x00
            })
    """
}


def gen_asus_board_name(board_group):
    if board_group[0] == "ROG" and board_group[1] == "STRIX":
        # fix WIFI name
        if board_group[-1].upper() == "WIFI":
            for chipset in ["B660", "X670"]:
                if board_group[2].startswith(chipset):
                    break
            else:
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
        if (
            len(board_group[3]) == 1 or
            board_group[3].upper() in ("PLUS", "PRO")
        ):
            board_group = [
                board_group[0], board_group[1],
                f"{board_group[2]}-{board_group[3]}"
            ] + board_group[4:]
        # create name
        board_name = f"{board_group[0]} {board_group[1]} "
        board_name += " ".join(board_group[2:])
    elif board_group[0].upper() in ("PRIME"):
        # fix WIFI name
        if board_group[-1].upper() == "WIFI":
            board_group[-1] = "(WI-FI)"
        # create name
        board_name = f"{board_group[0]} "
        board_name += "-".join(board_group[1:3]) + " "
        board_name += " ".join(board_group[3:])
    elif board_group[0] == "Pro" and board_group[1] == "WS":
        # create name
        board_name = f"{board_group[0]} {board_group[1]} "
        board_name += "-".join(board_group[2:])
    elif board_group[0].upper() in ("PRO", "PROART"):
        # create name
        board_name = f"{board_group[0]} "
        board_name += "-".join(board_group[1:])
    elif board_group[0].upper() in ("MAXIMUS", "TUF", "CROSSHAIR"):
        # create name
        board_name = f"{board_group[0]} "
        board_name += " ".join(board_group[1:])
    else:
        board_name = "-".join(board_group)
    board_name = board_name.replace("_", " ").strip()

    # conver board names
    if board_name.upper() in BOARDNAME_CONVERT:
        return BOARDNAME_CONVERT[board_name.upper()]
    return board_name


def gen_gigabyte_board_name(board_group):
    board_name = " ".join(board_group).upper()
    board_name = board_name.replace("_", " ").strip()

    # conver board names
    if board_name.upper() in BOARDNAME_CONVERT:
        return BOARDNAME_CONVERT[board_name.upper()]

    return board_name


def check_entrypoint(content, wmi_methods, uuid, method):
    if not check_method(content, ["WM" + method], count=3):
        return False
    method_for_search = uuid
    method_for_search += ":"
    for char in method:
        method_for_search += hex(ord(char)).upper()[2:]
    for wmi_method in wmi_methods:
        if wmi_method.startswith(method_for_search):
            return True
    return False


def check_gigabyte_entrypoint_method(content):
    method_template = "Method (_WDG, 0, Serialized)\n{\nReturn (QWDG)\n}"
    if method_template not in content:
        return False
    return True


def check_port(content):
    if "Name (IOHW, 0x0290)" not in content:
        return False
    if ", SystemIO, IOHW, 0x0A)" not in content:
        return False
    return True


def comments_remove(content):
    result = ""
    while True:
        # search comment start
        oneline_comment = content.find("//")
        if oneline_comment == -1:
            oneline_comment = len(content)
        multiline_comment = content.find("/*", 0, oneline_comment)
        if multiline_comment == -1:
            multiline_comment = len(content)
        # no comments in content
        if (
            multiline_comment == len(content) and
            oneline_comment == len(content)
        ):
            break
        # what is nearest
        if multiline_comment < oneline_comment:
            # skip uncommented
            result += content[:multiline_comment]
            content = content[multiline_comment + 2:]
            # search comment end
            multiline_comment = content.find("*/")
            if multiline_comment == -1:
                 multiline_comment = len(content)
            # skip */
            content = content[multiline_comment + 2:]
        else:
            # skip uncommented
            result += content[:oneline_comment]
            content = content[oneline_comment + 2:]
            # search comment end
            oneline_comment = content.find("\n")
            if oneline_comment == -1:
                 oneline_comment = len(content)
            # skip comment
            content = content[oneline_comment:]
    result += content
    return result


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


def code_clenaup(content):
    print (f"\tInitial size: {len(content)}")
    content = cleanup_lines(content)
    print (f"\tWhitespase clean: {len(content)}")
    content = comments_remove(content)
    print (f"\tComments clean: {len(content)}")
    content = cleanup_lines(content)
    print (f"\tRecleanup whitespace: {len(content)}")
    return content


def get_buffer_uuid_by_name(content, name):
    result = []
    while f"Name ({name}, Buffer (" in content:
        # search name buffer
        wdg_pos = content.find(f"Name ({name}, Buffer (")
        if wdg_pos == -1:
            wdg_pos = len(content) + 1
        # search buffer values start
        start_wdg = content.find("{", wdg_pos + 1)
        if start_wdg == -1:
            start_wdg = len(content) + 1
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


def check_custom_port(content):
    for line in content.split("\n"):
        if ", 0x0290)" in line and "Name (" in line:
            return True
    return False


def check_case(content, methods):
    for method in methods:
        method_hex = "".join([hex(ord(c))[2:] for c in method]).upper()
        method_imp = f"Case (0x{method_hex})\n{{\nReturn ({method} (Arg2))\n}}"
        if method_imp not in content:
            return False
    return True


def check_method(content, methods, count=1):
    for method in methods:
        if f"Method ({method}, {count}, Serialized)" not in content:
            return False
        if f"Method ({method}, {count}, Serialized)\n{{\nReturn (Ones)\n}}\n" in content:
            return False
    return True


def check_wmi(content):
    methods = ["RSEN", "GNAM", "GNUM", "UPSB", "GVER"]
    # RSEN 5253454E
    if "Case (0x52574543)" not in content:
        return False
    # GNAM 474E414D
    if "Case (0x51574543)" not in content:
        return False
    # GNUM 474E554D
    if "Case (0x50574543)" not in content:
        return False
    # UPSB 55505342
    if "Case (0x50574572)" not in content:
        return False
    # GVER 47564552
    if "Case (0x50574574)" not in content:
        return False
    if not check_method(content, methods):
        return False
    return True


def check_ec(content):
    methods = ["BREC"]
    if not check_case(content, methods):
        return False
    if not check_method(content, methods):
        return False
    return True


def check_nct6775(content):
    methods = ["RSIO", "WSIO", "RHWM", "WHWM"]
    if not check_case(content, methods):
        return False
    if not check_method(content, methods):
        return False
    return True


def check_nct6775_mutex(content):
    for mutex_name in ASUS_NCT6775_MUTEX:
        if f"If ((Acquire ({mutex_name}, 0xFFFF) == Zero))" in content:
            return mutex_name
    return ""


def check_ec_mutex(content):
    for mutex_name in ASUS_EC_MUTEX:
        if f"If ((Acquire ({mutex_name}, 0x03E8) == Zero))" in content:
            return mutex_name
    return ""


def set_default_flags(board_name, board_flags):
    board_flags.update({
        "asus_wmi": "N",
        "asus_ec": "N",
        "asus_wmi_port": "N",
        "asus_nct6775": "N",
        "asus_port290": "N",
        "gigabyte_wmi": "N",
        "asus_io_mutex": "",
        "asus_ec_mutex": "",
        "wmi_methods": [],
        "known_good": []
    })
    # set known io mutex name
    for mutex_name in ASUS_NCT6775_MUTEX:
        if board_name in ASUS_NCT6775_MUTEX[mutex_name]:
            board_flags["asus_io_mutex"] = mutex_name
    # set known io mutex name
    for mutex_name in ASUS_EC_MUTEX:
        if board_name in ASUS_EC_MUTEX[mutex_name]:
            board_flags["asus_ec_mutex"] = mutex_name


def update_board_flags(board_flags, content):

    # gigabyte
    if (
        check_gigabyte_entrypoint_method(content) and
        check_entrypoint(
            content, board_flags["wmi_methods"],
            "QWDG:DEADBEEF-2001-0000-00A0-C90629100000", "BB"
        )
    ):
        # already upstreamed
        if board_name in GIGABYTE_BOARDS:
            board_flags["gigabyte_wmi"] = "Y"
        else:
            board_flags["gigabyte_wmi"] = "U"

    # asus
    if check_entrypoint(
        content, board_flags["wmi_methods"],
        "_WDG:466747A0-70EC-11DE-8A39-0800200C9A66", "BD"
    ):
        board_flags["asus_wmi_port"] = "Y"

    # Check ec / can be without ntc6775 sensor
    if check_ec(content):
        board_ec_mutex = check_ec_mutex(content)
        if board_ec_mutex:
            board_flags["asus_ec_mutex"] = board_ec_mutex

        if board_name in EC_BOARDS:
            board_flags["asus_ec"] = "Y"
        else:
            board_flags["asus_ec"] = "U"

    # Check wmi / can be without ntc6775 sensor
    if check_wmi(content):
        if board_name in WMI_BOARDS:
            board_flags["asus_wmi"] = "Y"
        else:
            board_flags["asus_wmi"] = "U"

    # check nct6775
    if check_nct6775(content):
        # board can use unknown method of define port
        board_io_mutex = check_nct6775_mutex(content)
        if board_io_mutex:
            board_flags["asus_io_mutex"] = board_io_mutex

        if check_port(content):
            # already upstreamed
            if board_name in NCT6775_BOARDS:
                board_flags["asus_nct6775"] = "Y"
            else:
                board_flags["asus_nct6775"] = "U"
        elif check_custom_port(content):
            board_flags["asus_nct6775"] = "M"

    if check_custom_port(content):
        # recheck mossible mutex
        board_io_mutex = check_nct6775_mutex(content)
        if board_io_mutex:
            board_flags["asus_io_mutex"] = board_io_mutex

        board_flags["asus_port290"] = "Y"

    for name in KNOWN_GOOD_IMPLEMENTATION:
        if KNOWN_GOOD_IMPLEMENTATION[name] in content:
            if name not in board_flags["known_good"]:
                board_flags["known_good"].append(name)


def fix_flags(boards_flags):
    for board_name in boards_flags:
        board_flags = boards_flags[board_name]

        # check for errors in detect
        if (
            board_flags["gigabyte_wmi"] != "Y" and
            board_name in GIGABYTE_BOARDS
        ):
            board_flags["gigabyte_wmi"] += "?"

        if (
            board_flags["asus_wmi"] != "Y" and
            board_name in WMI_BOARDS
        ):
            board_flags["asus_wmi"] += "?"

        if (
            board_flags["asus_nct6775"] != "Y" and
            board_name in NCT6775_BOARDS
        ):
            board_flags["asus_nct6775"] += "?"

        if (
            board_flags["asus_nct6775"] in ("U", "Y") and
            board_flags["asus_wmi_port"] == "N"
        ):
            board_flags["asus_nct6775"] = "W"

        if (
            board_flags["asus_ec"] != "Y" and
            board_name in EC_BOARDS
        ):
            board_flags["asus_ec"] += "?"

        if (
            board_flags["asus_ec"] in ("U", "Y") and
            board_flags["asus_wmi_port"] == "N"
        ):
            board_flags["asus_ec"] = "W"

        # Workaround needed
        if (board_flags["asus_nct6775"] == "N" and
            board_flags["asus_wmi"] == "N" and
            board_flags["asus_ec"] == "N" and
            board_flags["asus_port290"] == "Y"
        ):
                board_flags["asus_nct6775"] = "P"

        if board_flags["known_good"]:
            board_flags["asus_nct6775"] += "K"


def add_load_flags(boards_flags):
    # boards with partial support, will be updated from mutext list
    nct6775_partial = []
    for mutex_name in ASUS_NCT6775_MUTEX:
        nct6775_partial += ASUS_NCT6775_MUTEX[mutex_name]
    for mutex_name in ASUS_EC_MUTEX:
        nct6775_partial += ASUS_EC_MUTEX[mutex_name]
    # validate load flags
    for board_name in sorted(
        NCT6775_BOARDS + WMI_BOARDS + EC_BOARDS + GIGABYTE_BOARDS + nct6775_partial
    ):
        # Just skip existed boards
        if board_name in boards_flags:
            continue
        boards_flags[board_name] = {
            "board_producer": "GIGABYTE" if board_name in GIGABYTE_BOARDS else "ASUS"
        }
        set_default_flags(board_name, boards_flags[board_name])
        boards_flags[board_name].update({
            "asus_wmi": "L" if board_name in WMI_BOARDS else "N",
            "gigabyte_wmi": "L" if board_name in GIGABYTE_BOARDS else "N",
            "asus_nct6775": "L" if board_name in (NCT6775_BOARDS + nct6775_partial) else "N",
            "asus_ec": "L" if board_name in EC_BOARDS else "N",
        })


def show_board(board_name, board_producer, asus_wmi="N", gigabyte_wmi="N",
               asus_nct6775="N", asus_ec="N", asus_io_mutex="", asus_ec_mutex=""):
    if asus_io_mutex:
        asus_nct6775 += " (" + asus_io_mutex + ")"
    if asus_ec_mutex:
        asus_ec += " (" + asus_ec_mutex + ")"
    return (
        f"| {board_producer}{' ' * (9 - len(board_producer))}"
        f"| {board_name}{' ' * (33 - len(board_name))}"
        f"| {asus_wmi}{' ' * (17 - len(asus_wmi)) }"
        f"| {gigabyte_wmi}{' ' * (13 - len(gigabyte_wmi)) }"
        f"| {asus_nct6775}{' ' * (30 - len(asus_nct6775))}"
        f"| {asus_ec}{' ' * (30 - len(asus_ec))}"
        f"|"
    )


def print_boards(boards_flags):
    table = {}
    boards2update_nct6775 = []

    for board_name in boards_flags:
        board_flags = boards_flags[board_name]

        if (
            "U" in board_flags["asus_nct6775"] and
            board_flags["asus_wmi"] == "N"
        ):
            for serie in NCT6775_SERIES:
                if board_name.upper().startswith(serie.upper()):
                    boards2update_nct6775.append(board_name)
                    break

    desc = show_board(
            board_name="board name",
            board_producer="made by",
            asus_wmi="asus_wmi_sensors",
            asus_nct6775="nct6775",
            asus_ec="asus_ec_sensors",
            gigabyte_wmi="gigabyte-wmi",
            asus_io_mutex="io mutex",
            asus_ec_mutex="ec mutex"
    )
    print(desc)
    desc = show_board(
            board_name="-" * 33,
            board_producer="-" * 9,
            asus_wmi="-" * 16,
            asus_nct6775="-"  * 29,
            asus_ec="-" * 29,
            gigabyte_wmi="-" * 12
    )
    print(desc)
    for board_name in sorted(boards_flags.keys()):
        board_flags = boards_flags[board_name]

        desc = show_board(
            board_name,
            board_producer=board_flags["board_producer"],
            asus_wmi=board_flags["asus_wmi"],
            asus_nct6775=board_flags["asus_nct6775"],
            asus_ec=board_flags["asus_ec"],
            gigabyte_wmi=board_flags["gigabyte_wmi"],
            asus_io_mutex=board_flags["asus_io_mutex"],
            asus_ec_mutex=board_flags["asus_ec_mutex"],
        )
        print (desc)

    print ("Boards with nct6775 to add:")
    for board_name in sorted(boards2update_nct6775):
        print (f"\t{board_name}")


if __name__ == "__main__":

    for name in KNOWN_GOOD_IMPLEMENTATION:
        KNOWN_GOOD_IMPLEMENTATION[name] = code_clenaup(
            KNOWN_GOOD_IMPLEMENTATION[name]
        )

    current_dir = "."
    if len(sys.argv) > 1:
        current_dir = sys.argv[1]

    boards_flags = {}

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
                board_producer = "ASUS"
                if board_group[-1].upper() in ("ASUS", "GIGABYTE"):
                    board_producer = board_group[-1].upper()
                    board_group = board_group[:-1]
                if board_producer == "GIGABYTE":
                    board_suffix = board_group[-1].split("_")
                    if len(board_suffix) >= 2:
                        board_version = board_suffix[-1]
                        board_group[-1] = "_".join(board_suffix[:-1])
                    board_name = gen_gigabyte_board_name(board_group)
                else:
                    board_name = gen_asus_board_name(board_group)

                print (f"Board: {board_name}")
                print (f"\tVersion: {board_version}")
                print (f"\tRevision: {board_hash}")
                print (f"\tProducer: {board_producer}")

                content = None
                with open(f"{dirname}/{filename}", "br") as f:
                    content = f.read().decode("utf8")

                if not content:
                    continue

                content = code_clenaup(content)

                # check dumps clenaup
                # with open(f"{dirname}/{filename}.tmp", "bw") as f:
                #    f.write(content.encode("utf8"))

                if board_name not in boards_flags:
                    boards_flags[board_name] = {
                        "board_producer": board_producer,
                    }
                    set_default_flags(board_name, boards_flags[board_name])
                board_flags = boards_flags[board_name]
                # get WMI methods:
                # Gigabyte: QWDG
                # ASUS: _WDG
                wmi_methods = []
                for buffer_name in ("_WDG", "QWDG"):
                    wmi_methods += get_buffer_uuid_by_name(content, buffer_name)
                str_methods = '\n\t\t'.join(wmi_methods)
                print (f"\tWMI methods: \n\t\t{str_methods}")
                # add methods to flags
                for wmi_method in wmi_methods:
                    if wmi_method not in board_flags["wmi_methods"]:
                        board_flags["wmi_methods"].append(wmi_method)
                # set other flags
                update_board_flags(board_flags, content)

    fix_flags(boards_flags)
    add_load_flags(boards_flags)
    print_boards(boards_flags)
    with open("boards.json", "wb") as f:
        f.write(json.dumps(boards_flags, indent=4).encode("utf8"))
