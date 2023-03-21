NCT6775_CHIPS = [
    "NCT5532",
    "NCT5538",
    "NCT5572",
    "NCT5573",
    "NCT5577",
    "NCT5582",
    "NCT6102",
    "NCT6104",
    "NCT6106",
    "NCT6116",
    "NCT6771",
    "NCT6772",
    "NCT6775",
    "NCT6776",
    "NCT6779",
    "NCT6791",
    "NCT6792",
    "NCT6793",
    "NCT6795",
    "NCT6796",
    "NCT6797",
    "NCT6798",
    "NCT6799",
    "W83677",
]

ASUS_BOARDS = {
    "A520": [
    ],
    "B360": [
    ],
    "B450": [
        "TUF GAMING B450-PLUS II",
        "B450M-DRAGON",
        "PRIME B450M-K",
        "PRIME B450M-K II",
        "PRIME B450M-A II",
        "TUF GAMING B450M-PRO II",
        "TUF GAMING B450M-PLUS II",
        "ROG STRIX B450-F GAMING II",
        "TUF GAMING B450M-PRO S",
        "ROG STRIX B450-E GAMING",
        "ROG STRIX B450-F GAMING",
        "ROG STRIX B450-I GAMING",
        "PRIME B450M-A",
        "TUF B450-PRO GAMING",
        "TUF B450M-PRO GAMING",
        "PRIME B450-PLUS",
        "TUF B450M-PLUS GAMING",
        "TUF B450-PLUS GAMING",
    ],
    "B460": [
    ],
    "B550": [
    ],
    "B650": [
    ],
    "B660": [
    ],
    "H410": [
        "PRIME H410M-K R2.0",
        "PRIME H410I-PLUS",
        "Pro H410T",
        "Pro H410M-C",
        "PRIME H410M-F",
        "PRIME H410I-PLUS",
        "EX-H410M-V3",
        "PRIME H410M-E",
        "PRIME H410M-A",
        "PRIME H410M-D",
        "PRIME H410M-K",
        "PRIME H410M-D",
        "PRIME H410M-E",
    ],
    "H510": [
    ],
    "H610": [
        "PRIME H610I-PLUS D4",
        "PRIME H610M-F D4",
        "PRIME H610M-A WIFI D4",
        "Pro H610M-CT D4",
        "Pro H610M-C D4",
        "Pro H610T D4",
        "Pro H610M-C",
        "PRIME H610M-D D4",
        "PRIME H610M-E D4",
        "PRIME H610M-K D4",
        "PRIME H610M-A D4",
        "EX-H610M-V3 D4",
    ],
    "W680": [
    ],
    "X570": [
        "TUF GAMING X570-PRO WIFI II",
        "ProArt X570-CREATOR WIFI",
        "ROG STRIX X570-E GAMING WIFI II",
        "ROG CROSSHAIR VIII EXTREME",
        "TUF GAMING X570-PLUS (WI-FI)",
        "ROG CROSSHAIR VIII DARK HERO",
        "TUF GAMING X570-PRO (WI-FI)",
        "PRIME X570-P",
        "TUF GAMING X570-PLUS",
        "PRIME X570-P",
        "PRIME X570-PRO",
        "ROG CROSSHAIR VIII FORMULA",
        "ROG CROSSHAIR VIII HERO",
        "ROG CROSSHAIR VIII HERO (WI-FI)",
        "ROG CROSSHAIR VIII IMPACT",
        "ROG STRIX X570-E GAMING",
        "ROG STRIX X570-F GAMING",
        "ROG STRIX X570-I GAMING",
    ],
    "X670": [
    ],
    "Z390": [
    ],
    "Z490": [
    ],
    "Z590": [
        "ROG STRIX Z590-A GAMING WIFI II",
        "PRIME Z590-P",
        "Z590 WIFI GUNDAM EDITION",
        "PRIME Z590-P WIFI",
        "ROG MAXIMUS XIII APEX",
        "PRIME Z590M-PLUS",
        "PRIME Z590-V",
        "TUF GAMING Z590-PLUS",
        "PRIME Z590-P",
        "ROG STRIX Z590-I GAMING WIFI",
        "ROG STRIX Z590-A GAMING WIFI",
        "ROG MAXIMUS XIII EXTREME",
        "PRIME Z590-A",
        "TUF GAMING Z590-PLUS WIFI",
        "ROG MAXIMUS XIII EXTREME GLACIAL",
        "ROG STRIX Z590-F GAMING WIFI",
        "ROG STRIX Z590-E GAMING WIFI",
        "ROG MAXIMUS XIII HERO",
    ],
    "Z690": [
    ],
    "Z790": [
    ],
}

BRIDGE_CHIPSETS = [
    # Intel LGA 1156
    "H55", "P55", "H57", "Q57",
    # Intel LGA 1155
    "H61", "B65", "Q65", "Q67", "H67", "P67", "Z68",
    "B75", "Q75", "Q77", "C216", "H77", "Z75", "Z77",
    # Intel LGA 1150
    "H81", "B85", "Q85", "Q87", "H87", "Z87",
    "H97", "Z97",
    # Intel LGA 1151
    "H110", "B150", "Q150", "H170", "C236", "Q170", "Z170",
    "B250", "Q250", "H270", "Q270", "Z270",
    "H310", "B365", "B360", "H370", "C246", "Q370", "Z370", "Z390",
    # Intel LGA 1200
    "H410", "B460", "H470", "Q470", "Z490", "W480",
    "H510", "B560", "H570", "Q570", "Z590", "W580",
    # Intel LGA 1700
    "H610", "B660", "H670", "Q670", "Z690", "W680",
    "B760", "H770", "Z790",
    # AMD FCH
    "A55T", "A50M", "A60M", "A68M", "A70M", "A76M",
    "A45", "A55", "A58", "A68H", "A75", "A78", "A85X", "A88X",
    "A55E", "A77E",
    # AMD AM4
    "A300",
    "X300",
    "Pro 500",
    "A320",
    "B350",
    "X370",
    "B450",
    "X470",
    "A520",
    "B550",
    "X570",
    # AMD TR4
    "X399",
    # AMD sTRX4
    "TRX40",
    # AMD sWRX8
    "WRX80",
    # AMD AM5
    "A620",
    "B650",
    "B650E",
    "X670",
    "X670E",
]
