#!/usr/bin/python3
import sys
import os
import copy
import json
import yaml
import time
import hashlib
import csv
from asl_parser import (
    parse_asl,
    cleanup_lines,
    asl_has_operator_with_params,
    search_block_with_name_parameter,
    asl_get_operator_with_params,
    decode_buffer_uuid_by_name,
)
from board_const import NCT6775_CHIPS, ASUS_BOARDS, BRIDGE_CHIPSETS
from utils import load_linuxhw_DMI, file_write_with_changes, load_board_flags


LINKS = []

# Upstreamed ec
EC_BOARDS = [
    "PRIME X470-PRO",
    "PRIME X570-PRO",
    "Pro WS X570-ACE",
    "ProArt X570-CREATOR WIFI",
    "ProArt B550-CREATOR",
    "ROG CROSSHAIR VIII DARK HERO",
    "ROG CROSSHAIR VIII HERO (WI-FI)",
    "ROG CROSSHAIR VIII FORMULA",
    "ROG CROSSHAIR VIII HERO",
    "ROG CROSSHAIR VIII IMPACT",
    "ROG CROSSHAIR X670E HERO",
    "ROG MAXIMUS XI HERO",
    "ROG MAXIMUS XI HERO (WI-FI)",
    "ROG STRIX B550-E GAMING",
    "ROG STRIX B550-I GAMING",
    "ROG STRIX X570-E GAMING",
    "ROG STRIX X570-E GAMING WIFI II",
    "ROG STRIX X570-F GAMING",
    "ROG STRIX X570-I GAMING",
    "ROG STRIX Z390-F GAMING",
    "ROG STRIX Z690-A GAMING WIFI D4",
    "ROG ZENITH II EXTREME",
    "ROG ZENITH II EXTREME ALPHA",
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
    # B550 style
    "B360M-BASALT",
    "B360M-D3H",
    "EX-B360M-V",
    "EX-B360M-V3",
    "EX-B360M-V5",
    "EX-B460M-V5",
    "EX-H410M-V3",
    "PRIME A520M-A",
    "PRIME A520M-A II",
    "PRIME A520M-E",
    "PRIME A520M-K",
    "PRIME B360-PLUS",
    "PRIME B360M-A",
    "PRIME B360M-C",
    "PRIME B360M-D",
    "PRIME B360M-K",
    "PRIME B460-PLUS",
    "PRIME B460I-PLUS",
    "PRIME B460M-A",
    "PRIME B460M-A R2.0",
    "PRIME B460M-K",
    "PRIME B550-PLUS",
    "PRIME B550-PLUS AC-HES",
    "PRIME B550M-A",
    "PRIME B550M-A (WI-FI)",
    "PRIME B550M-A AC",
    "PRIME B550M-A WIFI II",
    "PRIME B550M-K",
    "PRIME H310-PLUS",
    "PRIME H310I-PLUS",
    "PRIME H310M-A",
    "PRIME H310M-C",
    "PRIME H310M-D",
    "PRIME H310M-DASH",
    "PRIME H310M-E",
    "PRIME H310M-E/BR",
    "PRIME H310M-F",
    "PRIME H310M-K",
    "PRIME H310T",
    "PRIME H370-A",
    "PRIME H370-PLUS",
    "PRIME H370M-PLUS",
    "PRIME H410I-PLUS",
    "PRIME H410M-A",
    "PRIME H410M-D",
    "PRIME H410M-E",
    "PRIME H410M-F",
    "PRIME H410M-K",
    "PRIME H410M-K R2.0",
    "PRIME H410M-R",
    "PRIME H470-PLUS",
    "PRIME H470M-PLUS",
    "PRIME H510M-K R2.0",
    "PRIME Q370M-C",
    "PRIME X570-P",
    "PRIME X570-PRO",
    "PRIME Z390-A",
    "PRIME Z390-A/H10",
    "PRIME Z390-P",
    "PRIME Z390M-PLUS",
    "PRIME Z490-A",
    "PRIME Z490-P",
    "PRIME Z490-V",
    "PRIME Z490M-PLUS",
    "PRO B460M-C",
    "PRO H410M-C",
    "PRO H410T",
    "PRO Q470M-C",
    "Pro A520M-C",
    "Pro A520M-C II",
    "Pro B550M-C",
    "Pro WS X570-ACE",
    "ProArt B550-CREATOR",
    "ProArt X570-CREATOR WIFI",
    "ProArt Z490-CREATOR 10G",
    "ROG CROSSHAIR VIII DARK HERO",
    "ROG CROSSHAIR VIII EXTREME",
    "ROG CROSSHAIR VIII FORMULA",
    "ROG CROSSHAIR VIII HERO",
    "ROG CROSSHAIR VIII HERO (WI-FI)",
    "ROG CROSSHAIR VIII IMPACT",
    "ROG MAXIMUS XI APEX",
    "ROG MAXIMUS XI CODE",
    "ROG MAXIMUS XI EXTREME",
    "ROG MAXIMUS XI FORMULA",
    "ROG MAXIMUS XI GENE",
    "ROG MAXIMUS XI HERO",
    "ROG MAXIMUS XI HERO (WI-FI)",
    "ROG MAXIMUS XII APEX",
    "ROG MAXIMUS XII EXTREME",
    "ROG MAXIMUS XII FORMULA",
    "ROG MAXIMUS XII HERO (WI-FI)",
    "ROG STRIX B360-F GAMING",
    "ROG STRIX B360-G GAMING",
    "ROG STRIX B360-H GAMING",
    "ROG STRIX B360-H GAMING/OPTANE",
    "ROG STRIX B360-I GAMING",
    "ROG STRIX B460-F GAMING",
    "ROG STRIX B460-G GAMING",
    "ROG STRIX B460-H GAMING",
    "ROG STRIX B460-I GAMING",
    "ROG STRIX B550-A GAMING",
    "ROG STRIX B550-E GAMING",
    "ROG STRIX B550-F GAMING",
    "ROG STRIX B550-F GAMING (WI-FI)",
    "ROG STRIX B550-F GAMING WIFI II",
    "ROG STRIX B550-I GAMING",
    "ROG STRIX B550-XE GAMING WIFI",
    "ROG STRIX H370-F GAMING",
    "ROG STRIX H370-I GAMING",
    "ROG STRIX H470-I GAMING",
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
    "TUF B360-PLUS GAMING",
    "TUF B360-PRO GAMING",
    "TUF B360-PRO GAMING (WI-FI)",
    "TUF B360M-E GAMING",
    "TUF B360M-PLUS GAMING",
    "TUF B360M-PLUS GAMING S",
    "TUF B360M-PLUS GAMING/BR",
    "TUF GAMING A520M-PLUS",
    "TUF GAMING A520M-PLUS II",
    "TUF GAMING A520M-PLUS WIFI",
    "TUF GAMING B460-PLUS",
    "TUF GAMING B460-PRO (WI-FI)",
    "TUF GAMING B460M-PLUS",
    "TUF GAMING B460M-PLUS (WI-FI)",
    "TUF GAMING B460M-PRO",
    "TUF GAMING B550-PLUS",
    "TUF GAMING B550-PLUS (WI-FI)",
    "TUF GAMING B550-PLUS WIFI II",
    "TUF GAMING B550-PRO",
    "TUF GAMING B550M ZAKU (WI-FI)",
    "TUF GAMING B550M-E",
    "TUF GAMING B550M-E WIFI",
    "TUF GAMING B550M-PLUS",
    "TUF GAMING B550M-PLUS (WI-FI)",
    "TUF GAMING B550M-PLUS WIFI II",
    "TUF GAMING H470-PRO",
    "TUF GAMING H470-PRO (WI-FI)",
    "TUF GAMING X570-PLUS",
    "TUF GAMING X570-PLUS (WI-FI)",
    "TUF GAMING X570-PLUS_BR",
    "TUF GAMING X570-PRO (WI-FI)",
    "TUF GAMING X570-PRO WIFI II",
    "TUF GAMING Z490-PLUS",
    "TUF GAMING Z490-PLUS (WI-FI)",
    "TUF H310-PLUS GAMING",
    "TUF H310M-PLUS GAMING",
    "TUF H310M-PLUS GAMING/BR",
    "TUF H370-PRO GAMING",
    "TUF H370-PRO GAMING (WI-FI)",
    "TUF Z390-PLUS GAMING",
    "TUF Z390-PLUS GAMING (WI-FI)",
    "TUF Z390-PRO GAMING",
    "TUF Z390M-PRO GAMING",
    "TUF Z390M-PRO GAMING (WI-FI)",
    "WS Z390 PRO",
    "Z490-GUNDAM (WI-FI)",
    # B650 style
    "G15CF",
    "B560M-P",
    "EX-B560M-V5",
    "EX-B660M-V5 D4",
    "EX-B660M-V5 PRO D4",
    "EX-B760M-V5 D4",
    "EX-H510M-V3",
    "EX-H610M-V3 D4",
    "PRIME A620M-A",
    "PRIME B560-PLUS",
    "PRIME B560-PLUS AC-HES",
    "PRIME B560M-A",
    "PRIME B560M-A AC",
    "PRIME B560M-K",
    "PRIME B650-PLUS",
    "PRIME B650M-A",
    "PRIME B650M-A AX",
    "PRIME B650M-A AX II",
    "PRIME B650M-A II",
    "PRIME B650M-A WIFI",
    "PRIME B650M-A WIFI II",
    "PRIME B660-PLUS D4",
    "PRIME B660M-A AC D4",
    "PRIME B660M-A D4",
    "PRIME B660M-A WIFI D4",
    "PRIME B760-PLUS",
    "PRIME B760-PLUS D4",
    "PRIME B760M-A",
    "PRIME B760M-A AX D4",
    "PRIME B760M-A D4",
    "PRIME B760M-A WIFI",
    "PRIME B760M-A WIFI D4",
    "PRIME B760M-AJ D4",
    "PRIME B760M-K D4",
    "PRIME H510M-A",
    "PRIME H510M-A WIFI",
    "PRIME H510M-D",
    "PRIME H510M-E",
    "PRIME H510M-F",
    "PRIME H510M-K",
    "PRIME H510M-R",
    "PRIME H510T2/CSM",
    "PRIME H570-PLUS",
    "PRIME H570M-PLUS",
    "PRIME H610I-PLUS D4",
    "PRIME H610M-A D4",
    "PRIME H610M-A WIFI D4",
    "PRIME H610M-D D4",
    "PRIME H610M-E D4",
    "PRIME H610M-F D4",
    "PRIME H610M-K D4",
    "PRIME H610M-R D4",
    "PRIME H670-PLUS D4",
    "PRIME H770-PLUS D4",
    "PRIME X670-P",
    "PRIME X670-P WIFI",
    "PRIME X670E-PRO WIFI",
    "PRIME Z590-A",
    "PRIME Z590-P",
    "PRIME Z590-P WIFI",
    "PRIME Z590-V",
    "PRIME Z590M-PLUS",
    "PRIME Z690-A",
    "PRIME Z690-P",
    "PRIME Z690-P D4",
    "PRIME Z690-P WIFI",
    "PRIME Z690-P WIFI D4",
    "PRIME Z690M-PLUS D4",
    "PRIME Z790-A WIFI",
    "PRIME Z790-P",
    "PRIME Z790-P D4",
    "PRIME Z790-P WIFI",
    "PRIME Z790-P WIFI D4",
    "PRIME Z790M-PLUS",
    "PRIME Z790M-PLUS D4",
    "Pro B560M-C",
    "Pro B560M-CT",
    "Pro B660M-C",
    "Pro B660M-C D4",
    "Pro B760M-C",
    "Pro B760M-CT",
    "Pro H510M-C",
    "Pro H510M-CT",
    "Pro H610M-C",
    "Pro H610M-C D4",
    "Pro H610M-CT D4",
    "Pro H610T D4",
    "Pro Q670M-C",
    "Pro WS W680-ACE",
    "Pro WS W680-ACE IPMI",
    "Pro WS W790-ACE",
    "Pro WS W790E-SAGE SE",
    "ProArt B650-CREATOR",
    "ProArt B660-CREATOR D4",
    "ProArt B760-CREATOR D4",
    "ProArt X670E-CREATOR WIFI",
    "ProArt Z690-CREATOR WIFI",
    "ProArt Z790-CREATOR WIFI",
    "ROG CROSSHAIR X670E EXTREME",
    "ROG CROSSHAIR X670E GENE",
    "ROG CROSSHAIR X670E HERO",
    "ROG MAXIMUS XIII APEX",
    "ROG MAXIMUS XIII EXTREME",
    "ROG MAXIMUS XIII EXTREME GLACIAL",
    "ROG MAXIMUS XIII HERO",
    "ROG MAXIMUS Z690 APEX",
    "ROG MAXIMUS Z690 EXTREME",
    "ROG MAXIMUS Z690 EXTREME GLACIAL",
    "ROG MAXIMUS Z690 FORMULA",
    "ROG MAXIMUS Z690 HERO",
    "ROG MAXIMUS Z690 HERO EVA",
    "ROG MAXIMUS Z790 APEX",
    "ROG MAXIMUS Z790 EXTREME",
    "ROG MAXIMUS Z790 HERO",
    "ROG STRIX B560-A GAMING WIFI",
    "ROG STRIX B560-E GAMING WIFI",
    "ROG STRIX B560-F GAMING WIFI",
    "ROG STRIX B560-G GAMING WIFI",
    "ROG STRIX B560-I GAMING WIFI",
    "ROG STRIX B650-A GAMING WIFI",
    "ROG STRIX B650E-E GAMING WIFI",
    "ROG STRIX B650E-F GAMING WIFI",
    "ROG STRIX B650E-I GAMING WIFI",
    "ROG STRIX B660-A GAMING WIFI",
    "ROG STRIX B660-A GAMING WIFI D4",
    "ROG STRIX B660-F GAMING WIFI",
    "ROG STRIX B660-G GAMING WIFI",
    "ROG STRIX B660-I GAMING WIFI",
    "ROG STRIX B760-A GAMING WIFI",
    "ROG STRIX B760-A GAMING WIFI D4",
    "ROG STRIX B760-F GAMING WIFI",
    "ROG STRIX B760-G GAMING WIFI",
    "ROG STRIX B760-G GAMING WIFI D4",
    "ROG STRIX B760-I GAMING WIFI",
    "ROG STRIX X670E-A GAMING WIFI",
    "ROG STRIX X670E-E GAMING WIFI",
    "ROG STRIX X670E-F GAMING WIFI",
    "ROG STRIX X670E-I GAMING WIFI",
    "ROG STRIX Z590-A GAMING WIFI",
    "ROG STRIX Z590-A GAMING WIFI II",
    "ROG STRIX Z590-E GAMING WIFI",
    "ROG STRIX Z590-F GAMING WIFI",
    "ROG STRIX Z590-I GAMING WIFI",
    "ROG STRIX Z690-A GAMING WIFI",
    "ROG STRIX Z690-A GAMING WIFI D4",
    "ROG STRIX Z690-E GAMING WIFI",
    "ROG STRIX Z690-F GAMING WIFI",
    "ROG STRIX Z690-G GAMING WIFI",
    "ROG STRIX Z690-I GAMING WIFI",
    "ROG STRIX Z790-A GAMING WIFI",
    "ROG STRIX Z790-A GAMING WIFI D4",
    "ROG STRIX Z790-E GAMING WIFI",
    "ROG STRIX Z790-F GAMING WIFI",
    "ROG STRIX Z790-H GAMING WIFI",
    "ROG STRIX Z790-I GAMING WIFI",
    "TUF GAMING A620M-PLUS",
    "TUF GAMING A620M-PLUS WIFI",
    "TUF GAMING B560-PLUS WIFI",
    "TUF GAMING B560M-E",
    "TUF GAMING B560M-PLUS",
    "TUF GAMING B560M-PLUS WIFI",
    "TUF GAMING B650-PLUS",
    "TUF GAMING B650-PLUS WIFI",
    "TUF GAMING B650M-PLUS",
    "TUF GAMING B650M-PLUS WIFI",
    "TUF GAMING B660-PLUS WIFI D4",
    "TUF GAMING B660M-E D4",
    "TUF GAMING B660M-PLUS D4",
    "TUF GAMING B660M-PLUS WIFI",
    "TUF GAMING B660M-PLUS WIFI D4",
    "TUF GAMING B760-PLUS WIFI",
    "TUF GAMING B760-PLUS WIFI D4",
    "TUF GAMING B760M-BTF WIFI D4",
    "TUF GAMING B760M-E D4",
    "TUF GAMING B760M-PLUS",
    "TUF GAMING B760M-PLUS D4",
    "TUF GAMING B760M-PLUS WIFI",
    "TUF GAMING B760M-PLUS WIFI D4",
    "TUF GAMING H570-PRO",
    "TUF GAMING H570-PRO WIFI",
    "TUF GAMING H670-PRO WIFI D4",
    "TUF GAMING H770-PRO WIFI",
    "TUF GAMING X670E-PLUS",
    "TUF GAMING X670E-PLUS WIFI",
    "TUF GAMING Z590-PLUS",
    "TUF GAMING Z590-PLUS WIFI",
    "TUF GAMING Z690-PLUS",
    "TUF GAMING Z690-PLUS D4",
    "TUF GAMING Z690-PLUS WIFI",
    "TUF GAMING Z690-PLUS WIFI D4",
    "TUF GAMING Z790-PLUS D4",
    "TUF GAMING Z790-PLUS WIFI",
    "TUF GAMING Z790-PLUS WIFI D4",
    "Z590 WIFI GUNDAM EDITION",
]

# Upstreamed gigabyte
GIGABYTE_BOARDS = [
    "B450M DS3H-CF",
    "B450M DS3H WIFI-CF",
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
NCT6775_UPSTREAMED_CHIPSETS = [
    "A520",
    "A620",
    "B360",
    "B460",
    "B550",
    "B560",
    "B650",
    "B660",
    "B760",
    "H310",
    "H370",
    "H410",
    "H470",
    "H510",
    "H570",
    "H610",
    "H670",
    "H770",
    "W680",
    "W790",
    "Q370",
    "Q470",
    "Q670",
    "X570",
    "X670",
    "Z390",
    "Z490",
    "Z590",
    "Z690",
    "Z790",
]

# methods
EC_METHODS = ["BREC"]
NCT6775_METHODS = ["RSIO", "WSIO", "RHWM", "WHWM"]
NCT6775_REGION_METHODS = ["RHWM", "WHWM", "BRHM", "BWHM"]
WMI_METHODS = ["RSEN", "GNAM", "GNUM", "UPSB", "GVER"]
WMI_INT_METHODS = ["UPEC", "UPHM"]
WMI_METHODS_CONVERT = {
    "RSEN": "52574543",  # should be 5253454E
    "GNAM": "50574543",  # should be 474E414D
    "GNUM": "50574572",  # should be 474E554D
    "UPSB": "51574543",  # should be 55505342
    "GVER": "50574574",  # should be 47564552
}

# Bios dump has diffrent name to board name
BOARDNAME_CONVERT = {
    "PROART Z790-CREATOR-WIFI": "ProArt Z790-CREATOR WIFI",
    "PROART Z690-CREATOR-WIFI": "ProArt Z690-CREATOR WIFI",
    "PROART B660-CREATOR-D4": "ProArt B660-CREATOR D4",
    "PROART X670E-CREATOR-WIFI": "ProArt X670E-CREATOR WIFI",
    "PROART B550-CREATOR": "ProArt B550-CREATOR",
    "PROART X570-CREATOR-WIFI": "ProArt X570-CREATOR WIFI",
    "PROART Z490-CREATOR-10G": "ProArt Z490-CREATOR 10G",
    "ROG CROSSHAIR VI HERO WIFI AC": "ROG CROSSHAIR VI HERO (WI-FI AC)",
    "Z490-GUNDAM-WIFI": "Z490-GUNDAM (WI-FI)",
    "PRIME B450M-GAMING BR": "PRIME B450M-GAMING/BR",
    "PRIME X670-P (WI-FI)": "PRIME X670-P WIFI",
    "EX-B660M-V5-PRO-D4": "EX-B660M-V5 PRO D4",
    "PRO WS W680-ACE-IPMI": "Pro WS W680-ACE IPMI",
    "Z97-PRO-GAMER": "Z97-PRO GAMER",
    "Z170I-PRO-GAMING": "Z170I PRO GAMING",
    "Z170-PRO-GAMING-AURA": "Z170 PRO GAMING/AURA",
    "Z170-PRO-GAMING": "Z170 PRO GAMING",
    "H97-PRO-GAMER": "H97-PRO GAMER",
    "B85-PRO-GAMER": "B85-PRO GAMER",
    "B150-PRO-GAMING": "B150 PRO GAMING",
    "B150-PRO-GAMING-D3": "B150 PRO GAMING D3",
    "B150I-PRO-GAMING-AURA": "B150I PRO GAMING/AURA",
    "B150I-PRO-GAMING-WIFI-AURA": "B150I PRO GAMING/WIFI/AURA",
    "B150M-PRO-GAMING": "B150M PRO GAMING",
    "TUF GAMING A520M-PLUS (WI-FI)": "TUF GAMING A520M-PLUS WIFI",
    "PRO A520M-C": "Pro A520M-C",
    "PRO A520M-C-II": "Pro A520M-C II",
    "PROART B760-CREATOR-D4": "ProArt B760-CREATOR D4",
    "PRO A320M-R-WIFI": "PRO A320M-R WI-FI",
    "PRIME A320M-C R2": "PRIME A320M-C R2.0",
    "EX-B660M-V5-D4": "EX-B660M-V5 D4",
    "Z590-WIFI-GUNDAM-EDITION": "Z590 WIFI GUNDAM EDITION",
    "EX-B760M-V5-D4": "EX-B760M-V5 D4",
    "TUF B350M PLUS GAMING": "TUF B350M-PLUS GAMING",
    "TUF B450 PLUS GAMING": "TUF B450-PLUS GAMING",
    "PRIME B550-PLUS AC HES": "PRIME B550-PLUS AC-HES",
    "TUF GAMING B550M-E (WI-FI)": "TUF GAMING B550M-E WIFI",
    "PRIME B460M-A R2": "PRIME B460M-A R2.0",
    "TUF GAMING X570-PLUS BR": "TUF GAMING X570-PLUS_BR",
    "970-PRO-GAMING-AURA": "970 PRO GAMING/AURA",
    "B150-PRO-GAMING-AURA": "B150 PRO GAMING/AURA",
    "H170-PRO-GAMING": "H170 PRO GAMING",
    "X99-E-10G-WS": "X99-E-10G WS",
    "ROG STRIX B550-XE GAMING (WI-FI)": "ROG STRIX B550-XE GAMING WIFI",
    "PRIME H410M-K R2": "PRIME H410M-K R2.0",
    "PRO H610T-D4": "Pro H610T D4",
    "TUF B450M PRO GAMING": "TUF B450M-PRO GAMING",
    "TUF B450M PLUS GAMING": "TUF B450M-PLUS GAMING",
    "TUF B450 PRO GAMING": "TUF B450-PRO GAMING",
    "PRO H610M-CT-D4": "Pro H610M-CT D4",
    "PRO H610M-C-D4": "Pro H610M-C D4",
    "EX-H610M-V3-D4": "EX-H610M-V3 D4",
    "PRO B660M-C-D4": "Pro B660M-C D4",
    "PRO WS W790E-SAGE-SE": "Pro WS W790E-SAGE SE",
    "WS-Z390-PRO": "WS Z390 PRO",
    "TUF Z390 PLUS GAMING": "TUF Z390-PLUS GAMING",
    "TUF Z390 PLUS GAMING WIFI": "TUF Z390-PLUS GAMING (WI-FI)",
    "TUF Z390 PRO GAMING": "TUF Z390-PRO GAMING",
    "TUF Z390M PRO GAMING": "TUF Z390M-PRO GAMING",
    "TUF Z390M PRO GAMING WIFI": "TUF Z390M-PRO GAMING (WI-FI)",
    "PRIME B560-PLUS AC HES": "PRIME B560-PLUS AC-HES",
    "TUF B365 PLUS GAMING": "TUF B365-PLUS GAMING",
    "TUF B365M PLUS GAMING": "TUF B365M-PLUS GAMING",
    "PRIME H510M-K R2": "PRIME H510M-K R2.0",
    "PRIME Z390-A H10": "PRIME Z390-A/H10",
    "B250-MINING-EXPERT": "B250 MINING EXPERT",
    "B250M-C-PRO": "B250M-C PRO",
    "X99-E-WS-USB31": "X99-E WS/USB 3.1",
    "X99-E-WS": "X99-E WS",
    "B550M AORUS PRO P": "B550M AORUS PRO-P",
    "B450 AORUS PRO WIFI": "B450 AORUS PRO WIFI-CF",
    "B450M DS3H WIFI": "B450M DS3H WIFI-CF",
    "B450M DS3H": "B450M DS3H-CF",
    "PRIME A320M-K BR": "PRIME A320M-K/BR",
    "TUF GAMING B760M BTF WIFI D4": "TUF GAMING B760M-BTF WIFI D4",
    "PRIME H510T2-CSM": "PRIME H510T2/CSM",
    "ROG STRIX B360-H GAMING OPTANE": "ROG STRIX B360-H GAMING/OPTANE",
    "TUF B360M PLUS GAMING BR": "TUF B360M-PLUS GAMING/BR",
    "TUF B360 PLUS GAMING": "TUF B360-PLUS GAMING",
    "TUF B360 PRO GAMING": "TUF B360-PRO GAMING",
    "TUF B360 PRO GAMING WIFI": "TUF B360-PRO GAMING (WI-FI)",
    "TUF B360M PLUS GAMING S": "TUF B360M-PLUS GAMING S",
    "TUF B360M E GAMING": "TUF B360M-E GAMING",
    "TUF B360M PLUS GAMING": "TUF B360M-PLUS GAMING",
    "PRO WS WRX80E-SAGE-SE-WIFI": "Pro WS WRX80E-SAGE SE WIFI",
    "PRO WS WRX80E-SAGE-SE-WIFI-II": "Pro WS WRX80E-SAGE SE WIFI II",
    "Q370I-IM-A-R2": "Q370I-IM-A R2.0",
    "TUF H370 PRO GAMING": "TUF H370-PRO GAMING",
    "TUF H370 PRO GAMING WIFI": "TUF H370-PRO GAMING (WI-FI)",
    "WS C422 PRO SE": "WS C422 PRO/SE",
    "PRIME H310M-E BR": "PRIME H310M-E/BR",
    "TUF H310M PLUS GAMING R2": "TUF H310M-PLUS GAMING R2.0",
    "TUF H310M PLUS GAMING BR": "TUF H310M-PLUS GAMING/BR",
    "EX-H310M-V3-R2": "EX-H310M-V3 R2.0",
    "PRIME H310I-PLUS R2": "PRIME H310I-PLUS R2.0",
    "PRIME H310M-C PS R2": "PRIME H310M-C/PS R2.0",
    "PRIME H310M-CS R2": "PRIME H310M-CS R2.0",
    "PRIME H310M-DASH R2": "PRIME H310M-DASH R2.0",
    "PRIME H310M-R R2": "PRIME H310M-R R2.0",
    "PRIME H310T-R2": "PRIME H310T R2.0",
    "PRIME H310M-C R2": "PRIME H310M-C R2.0",
    "PRIME H310M-A R2": "PRIME H310M-A R2.0",
    "PRIME H310M-D R2": "PRIME H310M-D R2.0",
    "PRIME H310M-E R2": "PRIME H310M-E R2.0",
    "PRIME H310M-F R2": "PRIME H310M-F R2.0",
    "PRIME H310M-K R2": "PRIME H310M-K R2.0",
    "PRIME H310M-E R2 BR": "PRIME H310M-E R2.0/BR",
    "PRIME H310M2-R2": "PRIME H310M2 R2.0",
    "PRO H310M-R-R2-WIFI": "PRO H310M-R R2.0 WI-FI",
    "TUF H310 PLUS GAMING": "TUF H310-PLUS GAMING",
    "TUF H310M PLUS GAMING": "TUF H310M-PLUS GAMING",
    "PRIME H310-PLUS R2": "PRIME H310-PLUS R2.0",
}

ASUS_DISPATCHER = "WMBD"
GIGABYTE_DISPATCHER = "WMBB"

# mutex names from kernel source
ASUS_ITE87_MUTEX = {
    "\\AMW0._GL": [
        "CROSSHAIR VI HERO",  # "ASUSTeK Computer INC."
    ]
}

# mutex names from kernel source
ASUS_NCT6775_MUTEX = {
    "\\_SB.PC00.LPCB.SIO1.MUT0": [
        "ProArt B660-CREATOR D4",  # "ASUSTeK Computer INC."
        "ProArt Z790-CREATOR WIFI",  # "ASUSTeK Computer INC."
    ],
    "\\_SB.PCI0.LPCB.SIO1.MUT0": [
        "PRIME H410M-R",  # "ASUSTeK Computer INC."
    ],
    "\\_SB_.PCI0.LPCB.SIO1.MUT0": [
        "P8Z68-V LX",  # "ASUSTeK Computer INC."
        "MAXIMUS VII HERO",  # "ASUSTeK COMPUTER INC."
        "P8H67",  # "ASUSTeK COMPUTER INC."
        "ROG MAXIMUS X HERO",  # "ASUSTeK COMPUTER INC."
        "ROG STRIX Z370-H GAMING",  # "ASUSTeK COMPUTER INC."
        "Z170-DELUXE",  # "ASUSTeK COMPUTER INC."
        "Z170M-PLUS",  # "ASUSTeK COMPUTER INC."
    ],
    "\\_SB_.PCI0.LPC0.SIO1.MUT0": [
        "X99-E WS/USB 3.1",  # "ASUSTeK COMPUTER INC."
    ],
    "\\_SB.PCI0.SBRG.SIO1.MUT0": [
        "PRIME X370-PRO",  # "ASUSTeK COMPUTER INC."
        "PRIME X470-PRO",  # "ASUSTeK COMPUTER INC."
        "PRIME X399-A",  # "ASUSTeK COMPUTER INC."
        "PRIME B450-PLUS",  # "ASUSTeK COMPUTER INC." Need to recheck
        "PRIME Z270-A",  # "ASUSTeK COMPUTER INC."
        "PRIME Z370-A",  # "ASUSTeK COMPUTER INC."
        "CROSSHAIR VI HERO",  # "ASUSTeK COMPUTER INC."
        "ROG STRIX X399-E GAMING",  # "ASUSTeK COMPUTER INC."
        "ROG STRIX B350-F GAMING",  # "ASUSTeK COMPUTER INC."
        "ROG STRIX B450-F GAMING",  # "ASUSTeK COMPUTER INC."
        "TUF B450-PLUS GAMING",  # "ASUSTeK COMPUTER INC."
    ],
    "\\_GPE.MUT0": [
        "MAXIMUS IX APEX",  # "ASUSTeK COMPUTER INC." Need to recheck
    ],
}

ASUS_NCT6775_MUTEX_CODENAME = {
    "\\_SB.PCI0.LPCB.SIO1.MUT0": "acpi_board_ILPC_MUTEX",
    "\\_SB.PCI0.SBRG.SIO1.MUT0": "acpi_board_SBRG_MUTEX",
    "\\_SB_.PCI0.LPC0.SIO1.MUT0": "acpi_board_LPC0_MUTEX",
}


# mutex names from kernel source
ASUS_EC_MUTEX = {
    "\\AMW0.ASMX": [
        "ProArt X570-CREATOR WIFI",  # "ASUSTeK COMPUTER INC."
        "Pro WS X570-ACE",  # "ASUSTeK COMPUTER INC."
        "PRIME X570-PRO",  # "ASUSTeK COMPUTER INC."
        "ROG CROSSHAIR VIII DARK HERO",  # "ASUSTeK COMPUTER INC."
        "ROG CROSSHAIR VIII FORMULA",  # "ASUSTeK COMPUTER INC."
        "ROG CROSSHAIR VIII HERO",  # "ASUSTeK COMPUTER INC."
        "ROG CROSSHAIR VIII HERO (WI-FI)",  # "ASUSTeK COMPUTER INC."
        "ROG CROSSHAIR VIII IMPACT",  # "ASUSTeK COMPUTER INC."
        "ROG MAXIMUS XI HERO",  # "ASUSTeK COMPUTER INC."
        "ROG MAXIMUS XI HERO (WI-FI)",  # "ASUSTeK COMPUTER INC."
        "ROG STRIX B550-E GAMING",  # "ASUSTeK COMPUTER INC."
        "ROG STRIX B550-I GAMING",  # "ASUSTeK COMPUTER INC."
        "ROG STRIX X570-E GAMING",  # "ASUSTeK COMPUTER INC."
        "ROG STRIX X570-E GAMING WIFI II",  # "ASUSTeK COMPUTER INC."
        "ROG STRIX X570-F GAMING",  # "ASUSTeK COMPUTER INC."
        "ROG STRIX X570-I GAMING",  # "ASUSTeK COMPUTER INC."
    ],
    "\\RMTW.ASMX": [
        "ROG STRIX Z690-A GAMING WIFI D4",  # "ASUSTeK COMPUTER INC."
    ],
    "\\_SB_.PCI0.SBRG.SIO1.MUT0": [
        "ROG ZENITH II EXTREME",  # "ASUSTeK COMPUTER INC."
    ],
}

# Statuses for correctly detected board
BOARD_CORRECTLY_DETECTED = ("U", "Y", "L")

ASUS_KNOWN_UIDS = {
    "ASUSWMI": "B550 style board",
    "AsusMbSwInterface": "B650 style board",
}

ASUS_WIFI_NO_CONVERT = [
    "A620",
    "B560",
    "B650",
    "B660",
    "B760",
    "H510",
    "H570",
    "H670",
    "H770",
    "X670",
    "Z590",
    "Z690",
    "Z790",
]


def gen_asus_board_name(board_group):
    bridge_chipset = ""
    # remove SI at the end of name
    if board_group[-1].upper() == "SI":
        board_group = board_group[:-1]

    if board_group[0] == "ROG" and board_group[1] == "STRIX":
        # detect chipset from name
        for chipset in BRIDGE_CHIPSETS:
            if board_group[2].startswith(chipset):
                bridge_chipset = chipset
        # fix WIFI name
        if board_group[-1].upper() == "WIFI":
            for chipset in ASUS_WIFI_NO_CONVERT:
                if board_group[2].startswith(chipset):
                    break
            else:
                board_group[-1] = "(WI-FI)"
        # create name
        board_name = f"{board_group[0]} {board_group[1]} "
        board_name += f"{board_group[2]}-{board_group[3]} "
        board_name += " ".join(board_group[4:])
    elif board_group[0] == "ROG" and board_group[1] in (
        "CROSSHAIR",
        "MAXIMUS",
        "ZENITH",
        "RAMPAGE",
        "DOMINUS",
    ):
        # detect chipset from name
        for chipset in BRIDGE_CHIPSETS:
            if board_group[2].startswith(chipset):
                bridge_chipset = chipset
        # fix WIFI name
        if board_group[-1].upper() == "WIFI":
            board_group[-1] = "(WI-FI)"
        # create name
        board_name = f"{board_group[0]} {board_group[1]} "
        board_name += " ".join(board_group[2:])
    elif board_group[0] == "TUF" and board_group[1] == "GAMING":
        # detect chipset from name
        for chipset in BRIDGE_CHIPSETS:
            if board_group[2].startswith(chipset):
                bridge_chipset = chipset
        # fix WIFI name
        if board_group[-1].upper() == "WIFI":
            for chipset in ASUS_WIFI_NO_CONVERT:
                if board_group[2].startswith(chipset):
                    break
            else:
                board_group[-1] = "(WI-FI)"
        if len(board_group[3]) == 1 or board_group[3].upper() in ("PLUS", "PRO"):
            board_group = [
                board_group[0],
                board_group[1],
                f"{board_group[2]}-{board_group[3]}",
            ] + board_group[4:]
        # create name
        board_name = f"{board_group[0]} {board_group[1]} "
        board_name += " ".join(board_group[2:])
    elif board_group[0].upper() in ("PRIME", "STRIX"):
        # detect chipset from name
        for chipset in BRIDGE_CHIPSETS:
            if board_group[1].startswith(chipset):
                bridge_chipset = chipset
        # fix WIFI name
        if board_group[-1].upper() == "WIFI":
            for chipset in ASUS_WIFI_NO_CONVERT:
                if board_group[1].startswith(chipset):
                    break
            else:
                board_group[-1] = "(WI-FI)"
        # create name
        board_name = f"{board_group[0]} "
        board_name += "-".join(board_group[1:3]) + " "
        board_name += " ".join(board_group[3:])
        # for strix should be space before gaming
        if board_group[0].upper() in ("STRIX"):
            board_name = board_name.replace("-GAMING", " GAMING")
    elif board_group[0] == "Pro" and board_group[1] == "WS":
        # detect chipset from name
        for chipset in BRIDGE_CHIPSETS:
            if board_group[2].startswith(chipset):
                bridge_chipset = chipset
        # create name
        board_name = f"{board_group[0]} {board_group[1]} "
        board_name += "-".join(board_group[2:])
    elif board_group[0].upper() in ("PRO", "PROART"):
        # detect chipset from name
        for chipset in BRIDGE_CHIPSETS:
            if board_group[1].startswith(chipset):
                bridge_chipset = chipset
        # create name
        board_name = f"{board_group[0]} "
        board_name += "-".join(board_group[1:])
    elif board_group[0].upper() in ("MAXIMUS", "TUF", "CROSSHAIR", "RAMPAGE"):
        # detect chipset from name
        for chipset in BRIDGE_CHIPSETS:
            if board_group[1].startswith(chipset):
                bridge_chipset = chipset
        # create name
        board_name = f"{board_group[0]} "
        board_name += " ".join(board_group[1:])
    else:
        # detect chipset from name
        for chipset in BRIDGE_CHIPSETS:
            if bridge_chipset:
                break
            for board_name_part in board_group:
                if board_name_part.startswith(chipset):
                    bridge_chipset = chipset
                    break
        # just combine
        board_name = "-".join(board_group)
    board_name = board_name.replace("_", " ").strip()

    # conver board names
    if board_name.upper() in BOARDNAME_CONVERT:
        return BOARDNAME_CONVERT[board_name.upper()], bridge_chipset
    return board_name, bridge_chipset


def gen_gigabyte_board_name(board_group):
    board_name = " ".join(board_group).upper()
    board_name = board_name.replace("_", " ").strip()
    bridge_chipset = ""

    # detect chipset from name
    for chipset in BRIDGE_CHIPSETS:
        if bridge_chipset:
            break
        for board_name_part in board_group:
            if board_name_part.upper().startswith(chipset):
                bridge_chipset = chipset
                break

    # conver board names
    if board_name.upper() in BOARDNAME_CONVERT:
        return BOARDNAME_CONVERT[board_name.upper()], bridge_chipset

    return board_name, bridge_chipset


def check_asl_entrypoint(asl_struct, wmi_methods, uuid, method):
    if not check_asl_method(asl_struct, ["WM" + method], count=3):
        return False
    method_for_search = uuid
    method_for_search += ":"
    for char in method:
        method_for_search += hex(ord(char)).upper()[2:]
    for wmi_method in wmi_methods:
        if wmi_method.startswith(method_for_search):
            return True
    return False


def find_asl_methods_mutex(asl_struct, methods, known_mutexes, count=1):
    for method in methods:
        method_content = asl_get_operator_with_params(
            asl_struct, "Method", f"({method}, {count}, Serialized)"
        )
        if method_content:
            inline_mutex = get_asl_method_inline_mutexes(method_content)
            mutexes = get_asl_method_mutexes(method_content)
            for mutex_name in mutexes:
                if mutex_name in inline_mutex:
                    continue
                if mutex_name in known_mutexes:
                    return mutex_name
    return False


# get possible mutexes and filter by possible know as useful
def find_asl_mutex(asl_struct, known_mutexes):
    mutexes = search_block_with_name_parameter(
        asl_struct, {"operator": "Mutex"}, parent=False
    )
    for mutex_asl in mutexes:
        param = mutex_asl["parameters"]
        if param[0] != "(":
            continue
        mutex_name = param[1:].split(",")[0].strip()
        if mutex_name[0] != "\\" and mutex_asl["path"]:
            mutex_name = "\\" + ".".join(mutex_asl["path"] + [mutex_name])
        if mutex_name in known_mutexes:
            return mutex_name
    return False


def get_asl_nct6775_mutexes_in_block(asl_struct, region_name, known_mutexes):
    regions = search_block_with_name_parameter(
        asl_struct,
        {
            "operator": "OperationRegion",
            "parameters": f"({region_name}, SystemIO, IOHW, 0x0A)",
        },
    )
    for region in regions:
        methods = search_block_with_name_parameter(
            region, {"operator": "Method"}, parent=False
        )
        for method in methods:
            inline_mutex = get_asl_method_inline_mutexes(method)
            mutexes = get_asl_method_mutexes(method)
            for mutex_name in mutexes:
                if mutex_name in inline_mutex:
                    continue
                if mutex_name in known_mutexes:
                    return mutex_name
    return None


def check_asl_290_custom_port(asl_struct):
    ports = []
    for port_name in ["IO2B", "IO3B", "IOHB", "IOHW"]:
        if search_block_with_name_parameter(
            asl_struct, {"operator": "Name", "parameters": f"({port_name}, 0x0290)"}
        ):
            ports.append(port_name)
    return ports


def check_asl_290_port_region(asl_struct):
    for region_name in ["HWM", "SHWM", "HWRE"]:
        if not search_block_with_name_parameter(
            asl_struct,
            {
                "operator": "OperationRegion",
                "parameters": f"({region_name}, SystemIO, IOHW, 0x0A)",
            },
        ):
            continue
        if not search_block_with_name_parameter(
            asl_struct,
            {
                "operator": "Field",
                "parameters": f"({region_name}, ByteAcc, NoLock, Preserve)",
            },
        ):
            continue
        # for fields structure investigation
        for locked_state in ["Lock", "NoLock"]:
            index_blocks = search_block_with_name_parameter(
                asl_struct,
                {
                    "operator": "IndexField",
                    "parameters": f"(HIDX, HDAT, ByteAcc, {locked_state}, Preserve)",
                },
                parent=False,
            )
            index_blocks += search_block_with_name_parameter(
                asl_struct,
                {
                    "operator": "Field",
                    "parameters": f"({region_name}, ByteAcc, {locked_state}, Preserve)",
                },
                parent=False,
            )
            for block in index_blocks:
                index_content = block.get("content")
                # no index implementation
                if not index_content:
                    continue
                if region_name not in method_dumps:
                    method_dumps[region_name] = []
                if index_content not in method_dumps[region_name]:
                    method_dumps[region_name].append(index_content)
        return region_name
    return None


def check_asl_290_port(asl_struct):
    if not search_block_with_name_parameter(
        asl_struct,
        {"operator": "Name", "parameters": "(IOHW, 0x0290)"},  # probes 0x2e and 0x4e
    ):
        return False
    region_name = check_asl_290_port_region(asl_struct)
    if not region_name:
        # search region create in methods
        for method in NCT6775_REGION_METHODS:
            if method in NCT6775_METHODS:
                method_blocks = search_block_with_name_parameter(
                    asl_struct,
                    {"operator": "Method", "parameters": f"({method}, 1, Serialized)"},
                    parent=False,
                )
                for block in method_blocks:
                    func_impl = block.get("content")
                    # no method implementation
                    if not func_impl:
                        continue
                    # remove braces
                    if func_impl[0] != "{" or func_impl[-1] != "}":
                        continue
                    # parse asl
                    for sub_asl in parse_asl(func_impl[1:-1].strip()):
                        region_name = check_asl_290_port_region(sub_asl)
                        if region_name:
                            return region_name
    return region_name


def check_asl_case(asl_struct, dispatcher, methods, convert=None):
    method_content = asl_get_operator_with_params(
        asl_struct, "Method", f"({dispatcher}, 3, Serialized)"
    )
    if not method_content:
        return False
    func_impl = method_content.get("content")
    if not func_impl:
        return False
    for method in methods:
        if convert and convert.get(method):
            method_hex = convert.get(method)
        else:
            method_hex = "".join([hex(ord(c))[2:] for c in method]).upper()
        method_imp = f"Case (0x{method_hex})\n{{\nReturn ({method} (Arg2))\n}}"
        if method_imp not in func_impl:
            return False
    return True


method_dumps = {}


def check_asl_method(asl_struct, methods, count=1):
    for method in methods:
        if not asl_has_operator_with_params(
            asl_struct,
            {
                "operator": "Method",
                "parameters": f"({method}, {count}, Serialized)",
            },
        ):
            return False
        if asl_has_operator_with_params(
            asl_struct,
            {
                "operator": "Method",
                "parameters": f"({method}, {count}, Serialized)",
                "content": "{\nReturn (Ones)\n}",
            },
        ):
            return False
        method_content = asl_get_operator_with_params(
            asl_struct, "Method", f"({method}, {count}, Serialized)"
        )
        # no such method?
        if not method_content:
            return False
        func_impl = method_content.get("content")
        # no method implementation
        if not func_impl:
            return False
        # started with return zero?
        if func_impl.startswith("{\nReturn (Ones)"):
            return False
        if method not in method_dumps:
            method_dumps[method] = []
        if func_impl not in method_dumps[method]:
            method_dumps[method].append(func_impl)
    return True


def check_asl_methods_dispatcher(asl_struct, dispatcher, methods, convert=None):
    if not check_asl_case(asl_struct, dispatcher, methods, convert):
        return False
    if not check_asl_method(asl_struct, methods):
        return False
    return True


def get_asl_method_inline_mutexes(asl_struct):
    mutexes = []
    func_impl = asl_struct.get("content")
    while func_impl:
        start_mutex = func_impl.find("Mutex (")
        if start_mutex == -1:
            break
        end_mutex = func_impl.find(",", start_mutex)
        if end_mutex == -1:
            break
        mutex_name = func_impl[start_mutex + len("Mutex (") : end_mutex]
        func_impl = func_impl[end_mutex:]
        mutex_name = mutex_name.strip()
        if mutex_name[0] != "\\":
            mutex_name = "\\" + ".".join(asl_struct["path"] + [mutex_name])
        if mutex_name not in mutexes:
            mutexes.append(mutex_name)
    return mutexes


def get_asl_method_mutexes(asl_struct):
    mutexes = []
    func_impl = asl_struct.get("content")
    while func_impl:
        start_acquire = func_impl.find("Acquire (")
        if start_acquire == -1:
            break
        end_acquire = func_impl.find(",", start_acquire)
        if end_acquire == -1:
            break
        mutex_name = func_impl[start_acquire + len("Acquire (") : end_acquire]
        func_impl = func_impl[end_acquire:]
        mutex_name = mutex_name.strip()
        if mutex_name[0] != "\\" and asl_struct["path"]:
            mutex_name = "\\" + ".".join(asl_struct["path"] + [mutex_name])
        if mutex_name not in mutexes:
            mutexes.append(mutex_name)
    return mutexes


DEFAULT_FLAGS = {
    "asus_wmi": "N",
    "asus_ec": "N",
    "asus_wmi_entrypoint": "N",
    "asus_nct6775": "N",
    "asus_nct6775_region": "",
    "asus_port290": [],
    "asus_dispatcher": [],
    "gigabyte_wmi": "N",
    "asus_ite87_mutex": "",
    "asus_nct6775_mutex": "",
    "upstreamed_serie": False,
    "superio": "",
    "asus_ec_mutex": "",
    "bridge": "",
    "wmi_methods": [],
    "known_good": [],
    "known_good_nct6775": [],
    "links": [],
    "aliases": [],
    "system_name": "",
}


def set_default_flags(board_flags, board_name):
    # update flags to default
    for flag in DEFAULT_FLAGS:
        if flag not in board_flags:
            board_flags[flag] = copy.deepcopy(DEFAULT_FLAGS[flag])
    for key in board_flags.keys():
        if isinstance(board_flags[key], list):
            board_flags[key] = sorted(board_flags[key])

    if board_flags["gigabyte_wmi"] == "U" and board_name in GIGABYTE_BOARDS:
        if board_flags.get("hash"):
            board_flags["gigabyte_wmi"] = "Y"

    if board_flags["asus_wmi"] == "U" and board_name in WMI_BOARDS:
        if board_flags.get("hash"):
            board_flags["asus_wmi"] = "Y"

    if board_flags["asus_nct6775"] == "U" and board_name in NCT6775_BOARDS:
        if board_flags.get("hash"):
            board_flags["asus_nct6775"] = "Y"

    if board_flags["asus_ec"] == "U" and board_name in EC_BOARDS:
        if board_flags.get("hash"):
            board_flags["asus_ec"] = "Y"

    # set upstream ready
    if not board_flags["upstreamed_serie"]:
        if (
            "ASUS" in board_flags.get("board_producer")
            and board_flags.get("bridge") in NCT6775_UPSTREAMED_CHIPSETS
        ):
            board_flags["upstreamed_serie"] = True


def update_board_asl_flags(board_flags, asl_struct):
    # search name region Gigabyte style
    blocks = search_block_with_name_parameter(
        asl_struct, {"operator": "Name", "parameters": '(_UID, "GSADEV0")'}
    )
    for block in blocks:
        block_content = block["content"]
        if not asl_has_operator_with_params(
            block_content,
            {"operator": "Name", "parameters": '(_HID, EisaId ("PNP0C14") )'},
        ):
            continue
        # has convert _WDG -> QWDG
        if not asl_has_operator_with_params(
            block_content,
            {
                "operator": "Method",
                "parameters": "(_WDG, 0, Serialized)",
                "content": "{\nReturn (QWDG) \n}",
            },
        ):
            continue
        wdg_content = asl_get_operator_with_params(
            block_content, "Name", "(QWDG, Buffer ("
        )
        if wdg_content:
            wmi_methods = decode_buffer_uuid_by_name(wdg_content["parameters"], "QWDG")
            str_methods = "\n\t\t".join(wmi_methods)
            print(f"\tWMI methods: \n\t\t{str_methods}")
            # add methods to flags
            for wmi_method in wmi_methods:
                if wmi_method not in board_flags["wmi_methods"]:
                    board_flags["wmi_methods"].append(wmi_method)

        # check implementation
        if check_asl_entrypoint(
            block_content,
            board_flags["wmi_methods"],
            "QWDG:DEADBEEF-2001-0000-00A0-C90629100000",
            "BB",
        ) and check_asl_method(block_content, [GIGABYTE_DISPATCHER], count=3):
            # already upstreamed
            if board_name in GIGABYTE_BOARDS:
                board_flags["gigabyte_wmi"] = "Y"
            else:
                board_flags["gigabyte_wmi"] = "U"

    # port definition can be anywhere
    region_name = check_asl_290_port(asl_struct)
    if region_name:
        print(f"\tWMI port region name: {region_name}")
        board_flags["asus_nct6775_region"] = region_name
        mutex_name = get_asl_nct6775_mutexes_in_block(
            asl_struct, region_name, ASUS_NCT6775_MUTEX
        )
        if mutex_name:
            print(f"\tnct6775 io mutex in region: {mutex_name}")
            if not board_flags["asus_nct6775_mutex"]:
                board_flags["asus_nct6775_mutex"] = mutex_name

    port_names = check_asl_290_custom_port(asl_struct)
    if port_names:
        print(f"\tWMI ports names: {port_names}")
        board_flags["asus_port290"] = port_names
        if board_flags["asus_nct6775"] == "N":
            # port is defined in some custom way
            board_flags["asus_nct6775"] = "P"

    known_methods = sorted(
        EC_METHODS + WMI_METHODS + NCT6775_METHODS + NCT6775_REGION_METHODS
    )
    for dispatcher in [ASUS_DISPATCHER]:
        blocks = search_block_with_name_parameter(
            asl_struct,
            {"operator": "Method", "parameters": f"({dispatcher}, 3, Serialized)"},
        )
        for block in blocks:
            block_content = block["content"]
            for method in known_methods:
                if check_asl_methods_dispatcher(
                    block_content,
                    dispatcher=ASUS_DISPATCHER,
                    methods=[method],
                    convert=WMI_METHODS_CONVERT,
                ):
                    if method not in board_flags["asus_dispatcher"]:
                        board_flags["asus_dispatcher"].append(method)
        print(f'\t{dispatcher} dispatched methods: {board_flags["asus_dispatcher"]}')

    # search name in B550/B650 style
    for uid_name in ASUS_KNOWN_UIDS:
        blocks = search_block_with_name_parameter(
            asl_struct, {"operator": "Name", "parameters": f'(_UID, "{uid_name}")'}
        )
        for block in blocks:
            block_content = block["content"]
            if not asl_has_operator_with_params(
                block_content,
                {"operator": "Name", "parameters": '(_HID, EisaId ("PNP0C14") )'},
            ):
                continue

            if uid_name not in board_flags["known_good"]:
                board_flags["known_good"].append(uid_name)

            print(f"\tCan be: {ASUS_KNOWN_UIDS[uid_name]}")

            wdg_content = asl_get_operator_with_params(
                block_content, "Name", "(_WDG, Buffer ("
            )
            if wdg_content:
                wmi_methods = decode_buffer_uuid_by_name(
                    wdg_content["parameters"], "_WDG"
                )
                str_methods = "\n\t\t".join(wmi_methods)
                print(f"\tWMI methods: \n\t\t{str_methods}")
                # add methods to flags
                for wmi_method in wmi_methods:
                    if wmi_method not in board_flags["wmi_methods"]:
                        board_flags["wmi_methods"].append(wmi_method)

            # asus entrypoint
            if check_asl_entrypoint(
                block_content,
                board_flags["wmi_methods"],
                "_WDG:466747A0-70EC-11DE-8A39-0800200C9A66",
                "BD",
            ):
                board_flags["asus_wmi_entrypoint"] = "Y"

            # get ec method
            mutex_name = find_asl_methods_mutex(
                block_content, methods=EC_METHODS, known_mutexes=ASUS_EC_MUTEX
            )
            if mutex_name:
                print(f"\tEC mutex: {mutex_name}")
                board_flags["asus_ec_mutex"] = mutex_name

            # board can use unknown method of define port
            mutex_name = find_asl_methods_mutex(
                block_content, methods=NCT6775_METHODS, known_mutexes=ASUS_NCT6775_MUTEX
            )
            if mutex_name:
                print(f"\tNCT6775 mutex: {mutex_name}")
                board_flags["asus_nct6775_mutex"] = mutex_name

            # board can use unknown method of define port
            mutex_name = find_asl_methods_mutex(
                block_content,
                methods=WMI_INT_METHODS,
                known_mutexes=ASUS_ITE87_MUTEX,
                count=0,
            )
            if mutex_name:
                print(f"\tITE87 mutex: {mutex_name}")
                board_flags["asus_ite87_mutex"] = mutex_name

            # Check ec / can be without ntc6775 sensor
            if check_asl_methods_dispatcher(
                block_content, dispatcher=ASUS_DISPATCHER, methods=EC_METHODS
            ):
                print(f"\tEC methods by WMI Dispathcer: {EC_METHODS}")
                if board_name in EC_BOARDS:
                    board_flags["asus_ec"] = "Y"
                else:
                    board_flags["asus_ec"] = "U"

            # Check wmi / can be without ntc6775 sensor
            if check_asl_methods_dispatcher(
                block_content,
                dispatcher=ASUS_DISPATCHER,
                methods=WMI_METHODS,
                convert=WMI_METHODS_CONVERT,
            ):
                print(f"\tWMI methods by WMI Dispathcer: {WMI_METHODS}")
                if board_name in WMI_BOARDS:
                    board_flags["asus_wmi"] = "Y"
                else:
                    board_flags["asus_wmi"] = "U"

            # check nct6775
            if check_asl_methods_dispatcher(
                block_content,
                dispatcher=ASUS_DISPATCHER,
                methods=NCT6775_METHODS,
            ):
                if uid_name not in board_flags["known_good_nct6775"]:
                    board_flags["known_good_nct6775"].append(uid_name)

                print(
                    f"\tNCT6775 {uid_name} methods by WMI Dispathcer: {NCT6775_METHODS}"
                )
                if region_name:
                    # already upstreamed
                    if board_name in NCT6775_BOARDS:
                        board_flags["asus_nct6775"] = "Y"
                    else:
                        board_flags["asus_nct6775"] = "U"
                else:
                    board_flags["asus_nct6775"] = "M"
            # no other methods found
            elif region_name and board_flags["asus_nct6775"] == "N":
                # port is defined but no dispatch
                board_flags["asus_nct6775"] = "P"

    if (
        not board_flags.get("asus_nct6775_mutex")
        and board_flags.get("asus_nct6775") == "P"
    ):
        # board can use unknown method of define port
        mutex_name = find_asl_mutex(asl_struct, known_mutexes=ASUS_NCT6775_MUTEX)
        if mutex_name:
            print(f"\tNCT6775 partial mutex: {mutex_name}")
            board_flags["asus_nct6775_mutex"] = mutex_name


def fix_flags(boards_flags):
    for board_name in boards_flags:
        board_flags = boards_flags[board_name]

        set_default_flags(board_flags, board_name)

        # check for errors in detect
        if (
            board_flags["gigabyte_wmi"] not in BOARD_CORRECTLY_DETECTED
            and board_name in GIGABYTE_BOARDS
        ):
            if board_flags.get("hash"):
                board_flags["gigabyte_wmi"] += "?"
            else:
                board_flags["gigabyte_wmi"] = "L"

        if (
            board_flags["asus_wmi"] not in BOARD_CORRECTLY_DETECTED
            and board_name in WMI_BOARDS
        ):
            if board_flags.get("hash"):
                board_flags["asus_wmi"] += "?"
            else:
                board_flags["asus_wmi"] = "L"

        if (
            board_flags["asus_nct6775"] not in BOARD_CORRECTLY_DETECTED
            and board_name in NCT6775_BOARDS
        ):
            if board_flags.get("hash"):
                board_flags["asus_nct6775"] += "?"
            else:
                board_flags["asus_nct6775"] = "L"

        if (
            board_flags["asus_ec"] not in BOARD_CORRECTLY_DETECTED
            and board_name in EC_BOARDS
        ):
            if board_flags.get("hash"):
                board_flags["asus_ec"] += "?"
            else:
                board_flags["asus_ec"] = "L"

        if (
            board_flags["asus_ec"] in ("U", "Y")
            and board_flags["asus_wmi_entrypoint"] == "N"
        ):
            board_flags["asus_ec"] = "W"

        if (
            board_flags["asus_nct6775"] in ("U")
            and board_flags["asus_wmi"] in BOARD_CORRECTLY_DETECTED
        ):
            board_flags["asus_nct6775"] = "M"

        # set known io mutex name
        if not board_flags["asus_nct6775_mutex"]:
            for mutex_name in ASUS_NCT6775_MUTEX:
                if board_name in ASUS_NCT6775_MUTEX[mutex_name]:
                    board_flags["asus_nct6775_mutex"] = mutex_name

        # set known io mutex name
        if not board_flags["asus_ec_mutex"]:
            for mutex_name in ASUS_EC_MUTEX:
                if board_name in ASUS_EC_MUTEX[mutex_name]:
                    board_flags["asus_ec_mutex"] = mutex_name


def add_load_flags(boards_flags, board_desc):
    # boards with partial support, will be updated from mutext list
    nct6775_partial = []
    for mutex_name in ASUS_NCT6775_MUTEX:
        nct6775_partial += ASUS_NCT6775_MUTEX[mutex_name]
    for mutex_name in ASUS_EC_MUTEX:
        nct6775_partial += ASUS_EC_MUTEX[mutex_name]
    for bridge in ASUS_BOARDS:
        if bridge in NCT6775_UPSTREAMED_CHIPSETS:
            nct6775_partial += ASUS_BOARDS[bridge]
    # validate load flags
    boards_for_load = []
    for bridge in ASUS_BOARDS:
        boards_for_load += ASUS_BOARDS[bridge]
    boards_for_load += NCT6775_BOARDS
    boards_for_load += WMI_BOARDS
    boards_for_load += EC_BOARDS
    boards_for_load += GIGABYTE_BOARDS
    boards_for_load += nct6775_partial
    for board_name in sorted(boards_for_load):
        # Just skip existed boards
        if board_name in boards_flags:
            continue
        boards_flags[board_name] = {
            "board_producer": "Gigabyte Technology Co., Ltd."
            if board_name in GIGABYTE_BOARDS
            else "ASUSTeK COMPUTER INC."
        }
        set_default_flags(boards_flags[board_name], board_name)
        boards_flags[board_name].update(
            {
                "asus_wmi": "L" if board_name in WMI_BOARDS else "N",
                "gigabyte_wmi": "L" if board_name in GIGABYTE_BOARDS else "N",
                "asus_nct6775": "L"
                if board_name in (NCT6775_BOARDS + nct6775_partial)
                else "N",
                "asus_ec": "L" if board_name in EC_BOARDS else "N",
            }
        )

    # check load from db
    for board_info in board_desc:
        board_producer = board_info[0]
        board_name = board_info[1]
        board_superio = board_info[2]

        if not board_has_nct6775(board_superio):
            continue

        for serie in NCT6775_UPSTREAMED_CHIPSETS:
            # skip not asus for now
            if "ASUS" not in board_producer.upper():
                continue
            if serie in board_name.upper():
                if board_name not in boards_flags:
                    boards_flags[board_name] = {
                        "board_producer": board_producer,
                    }
                    set_default_flags(boards_flags[board_name], board_name)
                    boards_flags[board_name].update(
                        {
                            "asus_wmi": "N",
                            "gigabyte_wmi": "N",
                            "asus_nct6775": "L",
                            "asus_ec": "N",
                            "superio": board_superio,
                        }
                    )


def show_board(
    board_name,
    board_producer,
    superio="",
    asus_wmi="N",
    gigabyte_wmi="N",
    asus_nct6775="N",
    asus_ec="N",
    system_name="",
):
    if board_producer == "Hewlett-Packard":
        board_producer = "HP"
        # HP has product name in separate field
        if system_name:
            board_name = system_name
            if board_name.startswith("HP "):
                board_name = board_name[3:]
    else:
        for brand in ["ASUS", "GIGABYTE", "LENOVO", "ASROCK"]:
            if brand in board_producer.upper():
                board_producer = brand
                break
    return (
        f"| {board_producer}{' ' * (9 - len(board_producer))}"
        f"| {board_name}{' ' * (36 - len(board_name))}"
        f"| {superio}{' ' * (11 - len(superio))}"
        f"| {asus_wmi}{' ' * (13 - len(asus_wmi)) }"
        f"| {gigabyte_wmi}{' ' * (13 - len(gigabyte_wmi)) }"
        f"| {asus_nct6775}{' ' * (13 - len(asus_nct6775))}"
        f"| {asus_ec}{' ' * (13 - len(asus_ec))}"
        f"|"
    )


def board_has_nct6775(superio):
    if not superio:
        return True
    for chip_id in NCT6775_CHIPS:
        if superio.upper().startswith(chip_id):
            return True
    else:
        return False


def update_section(section, desc):
    with open("docs/nct6775-platform.c", "rb") as f:
        content = f.read().decode("utf8")
    if section == "ASUSWMI":
        search_code = "static const char * const asus_wmi_boards[] = {\n"
    elif section == "AsusMbSwInterface":
        search_code = "static const char * const asus_msi_boards[] = {\n"
    pos = content.find(search_code)
    if pos < 0:
        return
    result = content[: pos + len(search_code)]
    content = content[pos + len(search_code) :]
    result += desc
    pos = content.find("\n};\n")
    if pos < 0:
        return
    result += content[pos + 1 :]
    file_write_with_changes("docs/nct6775-platform.c", result.strip() + "\n")


def update_mutex_section(desc):
    with open("docs/nct6775-platform.c", "rb") as f:
        content = f.read().decode("utf8")
    search_code = "static const struct dmi_system_id asus_wmi_info_table[] = {\n"
    pos = content.find(search_code)
    if pos < 0:
        return
    result = content[: pos + len(search_code)]
    content = content[pos + len(search_code) :]
    result += desc
    pos = content.find("\n\t{}\n};\n")
    if pos < 0:
        return
    result += content[pos + 1 :]
    file_write_with_changes("docs/nct6775-platform.c", result.strip() + "\n")


def update_readme(desc):
    readme = ""
    with open("README.md", "rb") as f:
        readme = f.read().decode("utf8")
    replace_place_start = readme.find(desc.split("\n")[0])
    if replace_place_start < 0:
        return
    table_stop = False
    lines = readme[replace_place_start:].split("\n")
    readme = readme[:replace_place_start] + desc
    for line in lines:
        if table_stop:
            readme += line + "\n"
        else:
            if line.startswith("|"):
                continue
            else:
                table_stop = True
                readme += line + "\n"
    file_write_with_changes("README.md", readme.strip() + "\n")


def print_boards(boards_flags):
    table = {}
    nextgen_required = {}

    for board_name in boards_flags:
        board_flags = boards_flags[board_name]

        if board_flags.get("known_good_nct6775") and board_flags["asus_nct6775"] in (
            "M",
            "U",
            "Y",
        ):
            # nextgen patch required
            for name in board_flags["known_good_nct6775"]:
                if name not in nextgen_required:
                    nextgen_required[name] = []
                if board_name not in nextgen_required[name]:
                    nextgen_required[name].append(board_name)

    desc = ""
    desc += show_board(
        board_name="board name",
        board_producer="made by",
        superio="superio",
        asus_wmi="asus-wmi",
        asus_nct6775="nct6775",
        asus_ec="asus-ec",
        gigabyte_wmi="gigabyte-wmi",
    )
    desc += "\n"
    desc += show_board(
        board_name="-" * 35,
        board_producer="-" * 9,
        superio="-" * 10,
        asus_wmi="-" * 12,
        asus_nct6775="-" * 12,
        asus_ec="-" * 12,
        gigabyte_wmi="-" * 12,
    )
    desc += "\n"
    for board_name in sorted(boards_flags.keys()):
        board_flags = boards_flags[board_name]

        asus_wmi = board_flags["asus_wmi"]
        asus_nct6775 = board_flags["asus_nct6775"]
        if not board_flags.get("hash"):
            if board_flags.get("links"):
                asus_nct6775 = "F"
                asus_wmi = "F"
            else:
                asus_nct6775 = "L"
                asus_wmi = "L"
        desc += show_board(
            board_name,
            board_producer=board_flags["board_producer"],
            system_name=board_flags["system_name"],
            superio=board_flags["superio"],
            asus_wmi=asus_wmi,
            asus_nct6775=asus_nct6775,
            asus_ec=board_flags["asus_ec"],
            gigabyte_wmi=board_flags["gigabyte_wmi"],
        )
        desc += "\n"
    # print (desc)
    update_readme(desc)

    print("Boards with nct6775 for nextgen:")
    for name in nextgen_required:
        asus_wmi_section = ""
        for board_name in sorted(nextgen_required[name]):
            board_flags = boards_flags[board_name]

            if not board_has_nct6775(board_flags["superio"]):
                continue

            if board_flags["asus_nct6775"] == "M":
                asus_wmi_section += f'\t"{board_name}", // use custom port definition\n'
            elif not board_flags["upstreamed_serie"]:
                asus_wmi_section += f'\t"{board_name}", // No feedback\n'
            else:
                asus_wmi_section += f'\t"{board_name}",\n'
        update_section(name, asus_wmi_section)
        print(f"\tDevice name updated: '{name}'")
        # print (asus_wmi_section)

    print("Boards with nct6775 with mutex update")
    desc = ""
    for board_name in sorted(boards_flags.keys()):
        board_flags = boards_flags[board_name]

        if not board_has_nct6775(board_flags["superio"]):
            continue

        if (
            board_flags["asus_nct6775"] in ("P", "M")
            and board_flags["asus_nct6775_mutex"]
        ):
            if board_flags.get("board_producer") == "ASUSTeK Computer INC.":
                desc += (
                    f'\tDMI_MATCH_ASUS_NONWMI_BOARD("{board_name}", '
                    f'&{ASUS_NCT6775_MUTEX_CODENAME.get(board_flags["asus_nct6775_mutex"], "")}),\n'
                )
            elif board_flags.get("board_producer") == "ASUSTeK COMPUTER INC.":
                desc += (
                    f'\tDMI_MATCH_ASUS_WMI_BOARD("{board_name}", '
                    f'&{ASUS_NCT6775_MUTEX_CODENAME.get(board_flags["asus_nct6775_mutex"], "")}),\n'
                )
            elif board_flags.get("board_producer") == "ASRock":
                desc += (
                    f'\tDMI_MATCH_ASROCK_WMI_BOARD("{board_name}", '
                    f'&{ASUS_NCT6775_MUTEX_CODENAME.get(board_flags["asus_nct6775_mutex"], "")}),\n'
                )
    update_mutex_section(desc)


def file_name_to_board_name(filename, alias_to_name):
    board_group = filename.split("-")
    board_version = ""
    # check bios version
    if board_group[-1].isdigit():
        board_version = int(board_group[-1])
        board_group = board_group[:-1]
    # check board producer
    board_producer = "ASUS"
    if board_group[-1].upper() in ("ASUS", "GIGABYTE", "LENOVO", "HP"):
        board_producer = board_group[-1].upper()
        board_group = board_group[:-1]
    if board_producer == "GIGABYTE":
        board_suffix = board_group[-1].split("_")
        if len(board_suffix) >= 2:
            board_version = board_suffix[-1]
            board_group[-1] = "_".join(board_suffix[:-1])
        board_name, bridge_chipset = gen_gigabyte_board_name(board_group)
    else:
        board_name, bridge_chipset = gen_asus_board_name(board_group)

    # fix name by alias
    if filename in alias_to_name:
        board_name = alias_to_name[filename]

    # fix possible bridge detect error
    for bridge in ASUS_BOARDS:
        if board_name in ASUS_BOARDS[bridge]:
            bridge_chipset = bridge
            board_producer = "ASUS"

    if board_producer == "GIGABYTE":
        board_producer = "Gigabyte Technology Co., Ltd."
    elif board_producer == "ASUS":
        board_producer = "ASUSTeK COMPUTER INC."

    return board_name, board_version, bridge_chipset, board_producer


def update_superio_by_bridge(boards_flags):
    # update superio by bridge
    for bridge in ASUS_BOARDS:
        # current super io
        superio = ""
        producer = ""
        for board_name in ASUS_BOARDS[bridge]:
            if board_name in boards_flags:
                superio = boards_flags[board_name].get("superio")
                producer = boards_flags[board_name].get("board_producer")
                if superio:
                    break
        # skip serie
        if not superio:
            continue
        for board_name in ASUS_BOARDS[bridge]:
            if board_name not in boards_flags:
                boards_flags[board_name] = {
                    "board_producer": producer,
                }
                set_default_flags(boards_flags[board_name], board_name)
            boards_flags[board_name]["bridge"] = bridge
            if not boards_flags[board_name].get("superio"):
                boards_flags[board_name]["superio"] = superio


if __name__ == "__main__":
    # resort board names
    for chip in ASUS_BOARDS:
        names = []
        for name in ASUS_BOARDS[chip]:
            if name not in names:
                names.append(name)
        ASUS_BOARDS[chip] = sorted(names)

    print("Known boards bridges")
    print(json.dumps(ASUS_BOARDS, sort_keys=True, indent=4))

    current_dir = "."
    if len(sys.argv) > 1:
        current_dir = sys.argv[1]

    count_files = 0
    for dirname, _, filenames in os.walk(current_dir):
        # print path to all filenames.
        for filename in filenames:
            if filename.endswith(".dsl"):
                count_files += 1

    board_desc = []
    alias_to_name = {}
    boards_flags = load_board_flags()

    # remove boards with old name
    for board_name in BOARDNAME_CONVERT:
        if board_name in boards_flags:
            del boards_flags[board_name]

    for board_name in sorted(boards_flags.keys()):
        # skip boards with different cases
        if board_name == BOARDNAME_CONVERT.get(board_name.upper()):
            continue
        # fully diffent names
        if board_name.upper() in BOARDNAME_CONVERT:
            del boards_flags[board_name]

    # create aliases base
    for name in boards_flags:
        set_default_flags(boards_flags[name], name)
        aliases = boards_flags[name].get("aliases", [])
        for alias in aliases:
            alias_to_name[alias] = name
        board_flags = boards_flags[name]
        if (
            board_has_nct6775(board_flags["superio"])
            and board_flags.get("asus_wmi_entrypoint") == "Y"
            and not board_flags.get("known_good")
            and not board_flags.get("known_good_nct6775")
        ):
            board_flags["hash"] = []
            print(f"Need revalidate {name}")

    for board_load_link in LINKS:
        filename = board_load_link.split("/")[-1]
        file_parts = filename.split(".")
        if len(file_parts) != 2:
            print(f"Uknown file name format: {filename}")
            continue
        if file_parts[-1].lower() != "zip":
            print(f"Not zip? {file_parts[-1]}")
            continue
        # gigabyte fix
        for prefix in ["mb_bios_", "b_bios_"]:
            if file_parts[0].startswith(prefix):
                file_parts[0] = file_parts[0][len(prefix) :] + "-GIGABYTE"
        # convert names
        (
            board_name,
            board_version,
            bridge_chipset,
            board_producer,
        ) = file_name_to_board_name(file_parts[0], alias_to_name)

        # create flags struct
        if board_name not in boards_flags:
            boards_flags[board_name] = {
                "board_producer": board_producer,
            }
        board_flags = boards_flags[board_name]
        set_default_flags(board_flags, board_name)
        if bridge_chipset:
            board_flags["bridge"] = bridge_chipset
        # links
        if not board_flags.get("links"):
            board_flags["links"] = []
        if board_load_link not in board_flags["links"]:
            board_flags["links"].append(board_load_link)
        board_flags["links"] = sorted(board_flags["links"])
        # aliases
        if not board_flags.get("aliases"):
            board_flags["aliases"] = []
        if file_parts[0] not in board_flags["aliases"]:
            board_flags["aliases"].append(file_parts[0])
        board_flags["aliases"] = sorted(board_flags["aliases"])

        print(f"To {board_name} added {board_load_link}")

    try:
        with open("methods.json", "rb") as f:
            method_dumps.update(json.loads(f.read().decode("utf8")))
    except Exception as ex:
        print(f"Could not read methods.json: {ex}")

    # Load linux hw DMI database
    for row in load_linuxhw_DMI():
        if row[0] not in (
            "ASUSTeK Computer INC.",
            "ASUSTeK COMPUTER INC.",
            "ASRock",
            "Gigabyte Technology Co., Ltd.",
            "Hewlett-Packard",
            "LENOVO",
        ):
            continue
        board_desc.append(row)
    print(f"Loaded cleanuped {len(board_desc)} boards descriptions.")

    # update superio
    for board_name in boards_flags:
        board_flags = boards_flags[board_name]
        # set chip value strict
        for board_info in board_desc:
            if (
                board_info[0] == board_flags["board_producer"]
                and board_info[1].upper() == board_name.upper()
            ):
                if board_info[2]:
                    board_flags["superio"] = board_info[2]
                if board_info[1] != board_name:
                    print(
                        f"\tDatabase has different name {board_info[1]} != {board_name}"
                    )
                break

    processed_files = 0
    for dirname, _, filenames in os.walk(current_dir):
        # print path to all filenames.
        for filename in filenames:
            if filename.endswith(".dsl"):
                file_parts = filename.split(".")
                if len(file_parts) != 3:
                    print(f"Can't parse filename: '{dirname}/{filename}'")

                board_hash = file_parts[1]

                (
                    board_name,
                    board_version,
                    bridge_chipset,
                    board_producer,
                ) = file_name_to_board_name(file_parts[0], alias_to_name)

                processed_files += 1
                print(f"Board: {board_name}")
                print(f"Progress: {round(processed_files * 100 / count_files, 2)}%")
                print(f"\tVersion: {board_version}")
                print(f"\tRevision: {board_hash}")
                print(f"\tProducer: {board_producer}")

                content = None
                with open(f"{dirname}/{filename}", "br") as f:
                    content = f.read().decode("utf8")

                if not content:
                    continue

                start_time = time.time()
                print(f"\tInitial size: {len(content)}")
                # create flags struct
                if board_name not in boards_flags:
                    boards_flags[board_name] = {
                        "board_producer": board_producer,
                    }
                board_flags = boards_flags[board_name]
                set_default_flags(board_flags, board_name)
                if bridge_chipset:
                    board_flags["bridge"] = bridge_chipset

                # aliases
                if not board_flags.get("aliases"):
                    board_flags["aliases"] = []
                if file_parts[0] not in board_flags["aliases"]:
                    board_flags["aliases"].append(file_parts[0])
                board_flags["aliases"] = sorted(board_flags["aliases"])

                set_default_flags(board_flags, board_name)

                # set chip value strict
                for board_info in board_desc:
                    if (
                        board_info[0] == board_flags["board_producer"]
                        and board_info[1].upper() == board_name.upper()
                    ):
                        board_flags["superio"] = board_info[2]
                        print(f"\tSuper I/O: {board_info[2]}")
                        if len(board_info) > 4:
                            board_flags["system_name"] = board_info[4]
                        if board_info[1] != board_name:
                            print(
                                f"\tDatabase has different name {board_info[1]} != {board_name}"
                            )
                        break

                # set chip value like base version
                if not board_flags["superio"]:
                    for board_info in board_desc:
                        if board_info[0] == board_flags[
                            "board_producer"
                        ] and board_name.upper().startswith(board_info[1].upper()):
                            if board_info[2]:
                                board_flags["superio"] = board_info[2]
                                print(f"\tSuper I/O: {board_info[2]}")
                                break

                if not board_flags.get("hash"):
                    board_flags["hash"] = []
                else:
                    # clean up hashes
                    hashes = []
                    for content_hash in board_flags["hash"]:
                        if content_hash not in hashes:
                            hashes.append(content_hash)
                    board_flags["hash"] = hashes

                content_without_file_name = "\n".join(
                    [
                        line
                        for line in content.split("\n")
                        if not line.startswith(" * Disassembly of ")
                    ]
                )

                content_hash = hashlib.md5(
                    content_without_file_name.encode("utf-8")
                ).hexdigest()
                print(f"\tmd5: {content_hash}")

                if content_hash in board_flags["hash"]:
                    continue

                board_flags["hash"].append(content_hash)

                # content cleanup and convert
                content = cleanup_lines(content)

                asl_struct = parse_asl(content)
                if os.environ.get("DEBUG"):
                    # check dumps clenaup
                    with open(
                        f"{dirname}/{file_parts[0]}.{file_parts[1]}.json", "bw"
                    ) as f:
                        f.write(json.dumps(asl_struct, indent=4).encode("utf8"))

                update_board_asl_flags(board_flags, asl_struct)

                print(f"\tProcess time: {round(time.time() - start_time, 3)}")

    update_superio_by_bridge(boards_flags)

    # sort flags
    for name in boards_flags:
        set_default_flags(boards_flags[name], name)

    # save current state
    file_write_with_changes("boards.yaml", yaml.dump(boards_flags))
    file_write_with_changes("methods.json", json.dumps(method_dumps, indent=4))
    # show results
    add_load_flags(boards_flags, board_desc)
    fix_flags(boards_flags)
    print(f"Boards: {len(boards_flags.keys())}")
    print_boards(boards_flags)
