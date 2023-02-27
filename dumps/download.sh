#!/bin/bash

# asus bioses
mkdir -p ASUS
cd ASUS
# download capsules
for bios_file in \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/CROSSHAIR-VI-HERO-ASUS-8601.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/EX-A320M-GAMING-SI-6061.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/EX-B660M-V5-D4-SI-2214.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/EX-B660M-V5-PRO-D4-SI-2015.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/EX-B760M-V5-D4-SI-0808.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/MAXIMUS-IX-EXTREME-ASUS-1501.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-A320I-K-ASUS-6061.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-A320M-A-ASUS-6061.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-A320M-C-R2-SI-6061.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-A320M-E-ASUS-6061.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-A320M-F-SI-6061.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-A320M-K-ASUS-6061.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-A520M-A-ASUS-3001.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-A520M-A-II-ASUS-3001.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-A520M-E-ASUS-3001.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-A520M-K-ASUS-2814.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B350M-A-ASUS-6061.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B350M-E-ASUS-6061.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B350M-K-ASUS-6061.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B350-PLUS-ASUS-6061.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B360-PLUS-ASUS-3101.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B450M-GAMING-BR-SI-3804.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B450M-GAMING-II-ASUS-3802.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B450-PLUS-ASUS-3802.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B460-PLUS-ASUS-1620.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B550M-A-AC-ASUS-2803.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B550M-A-ASUS-2803.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B550M-A-WIFI-ASUS-2803.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B550M-A-WIFI-II-ASUS-2803.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B550M-K-ASUS-2803.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B550-PLUS-ASUS-2803.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B650M-A-ASUS-0812.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B650M-A-ASUS-0821.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B650M-A-AX-ASUS-0821.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B650M-A-AX-II-ASUS-1222.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B650M-A-II-ASUS-0303.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B650M-A-WIFI-ASUS-0812.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B650M-A-WIFI-II-ASUS-0303.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B650-PLUS-ASUS-0809.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B650-PLUS-ASUS-0823.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B660M-A-D4-ASUS-2014.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B660M-A-WIFI-D4-ASUS-2014.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B760M-A-AX-D4-ASUS-0405.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B760M-A-D4-ASUS-0405.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B760M-A-D4-ASUS-0807.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B760M-AJ-D4-ASUS-0807.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B760M-A-WIFI-D4-ASUS-0807.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B760M-K-D4-ASUS-0807.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B760-PLUS-D4-ASUS-0807.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-H410M-R-ASUS-1620.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-X370-PRO-ASUS-6042.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-X399-A-ASUS-1206.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-X470-PRO-ASUS-6042.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-X570-P-ASUS-4021.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-X570-PRO-ASUS-4021.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-X670E-PRO-WIFI-ASUS-0821.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-X670-P-ASUS-0823.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-X670-P-WIFI-ASUS-0823.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-Z270M-PLUS-ASUS-2001.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-Z270-P-ASUS-2001.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-Z370-A-ASUS-3004.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-Z370-A-II-ASUS-3004.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-Z590-A-ASUS-1701.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-Z590M-PLUS-ASUS-1801.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-Z590-P-ASUS-1801.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-Z590-P-WIFI-ASUS-1801.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-Z590-V-ASUS-1801.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRO-A320M-R-WIFI-SI-6061.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/Pro-A520M-C-II-SI-3001.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRO-A520M-C-SI-3001.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ProArt-B550-CREATOR-ASUS-2803.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ProArt-B650-CREATOR-ASUS-0922.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ProArt-B660-CREATOR-D4-ASUS-2103.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ProArt-B760-CREATOR-D4-ASUS-0812.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PROART-X570-CREATOR-WIFI-ASUS-0801.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ProArt-X670E-CREATOR-WIFI-ASUS-0705.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ProArt-Z490-CREATOR-10G-ASUS-2601.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ProArt-Z690-CREATOR-WIFI-ASUS-2103.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ProArt-Z790-CREATOR-WIFI-ASUS-0703.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/Pro-B550M-C-SI-2423.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/Pro-B550M-C-SI-2804.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/Pro-B660M-C-D4-ASUS-2014.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/Pro-B660M-C-SI-2212.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/Pro-B760M-C-SI-0405.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/Pro-B760M-CT-SI-0402.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRO-H410T-SI-1623.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/Pro-WS-W680-ACE-ASUS-0203.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/Pro-WS-W680-ACE-IPMI-ASUS-0203.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/Pro-WS-X570-ACE-ASUS-4201.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-CROSSHAIR-VI-EXTREME-ASUS-8601.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-CROSSHAIR-VI-HERO-WIFI-AC-ASUS-8601.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-CROSSHAIR-VII-HERO-ASUS-4901.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-CROSSHAIR-VII-HERO-WIFI-ASUS-4901.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-CROSSHAIR-VIII-DARK-HERO-ASUS-4201.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-CROSSHAIR-VIII-EXTREME-ASUS-0801.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-CROSSHAIR-VIII-FORMULA-ASUS-4201.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-CROSSHAIR-VIII-HERO-ASUS-4201.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-CROSSHAIR-VIII-HERO-WIFI-ASUS-4201.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-CROSSHAIR-VIII-IMPACT-ASUS-4201.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-CROSSHAIR-X670E-EXTREME-ASUS-0705.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-CROSSHAIR-X670E-EXTREME-ASUS-0805.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-CROSSHAIR-X670E-GENE-ASUS-0705.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-CROSSHAIR-X670E-GENE-ASUS-0805.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-CROSSHAIR-X670E-HERO-ASUS-0705.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-CROSSHAIR-X670E-HERO-ASUS-0805.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-MAXIMUS-X-HERO-ASUS-2701.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-MAXIMUS-XI-HERO-ASUS-2004.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-MAXIMUS-XI-HERO-WIFI-ASUS-2004.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-MAXIMUS-XIII-APEX-ASUS-1701.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-MAXIMUS-XIII-EXTREME-ASUS-1701.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-MAXIMUS-XIII-EXTREME-GLACIAL-ASUS-1402.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-MAXIMUS-XIII-EXTREME-GLACIAL-ASUS-1701.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-MAXIMUS-XIII-HERO-ASUS-1701.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-MAXIMUS-Z690-EXTREME-ASUS-2103.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-MAXIMUS-Z690-EXTREME-GLACIAL-ASUS-2103.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-MAXIMUS-Z790-EXTREME-ASUS-0703.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B350-F-GAMING-ASUS-5606.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B350-F-GAMING-ASUS-6061.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B350-I-GAMING-ASUS-5606.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B350-I-GAMING-ASUS-6061.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B450-E-GAMING-ASUS-4602.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B450-F-GAMING-ASUS-4602.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B450-F-GAMING-II-ASUS-4602.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B450-I-GAMING-ASUS-4602.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B550-A-GAMING-ASUS-2423.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B550-E-GAMING-ASUS-2423.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B550-F-GAMING-ASUS-2423.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B550-F-GAMING-WIFI-ASUS-2423.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B550-F-GAMING-WIFI-II-ASUS-0305.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B550-F-GAMING-WIFI-II-ASUS-2803.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B550-I-GAMING-ASUS-2423.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B550-XE-GAMING-WIFI-ASUS-2425.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B650-A-GAMING-WIFI-ASUS-0823.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B650E-E-GAMING-WIFI-ASUS-0804.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B650E-E-GAMING-WIFI-ASUS-0821.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B650E-F-GAMING-WIFI-ASUS-0804.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B650E-F-GAMING-WIFI-ASUS-0821.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B650E-I-GAMING-WIFI-ASUS-0821.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B660-A-GAMING-WIFI-ASUS-2212.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B660-A-GAMING-WIFI-D4-ASUS-2015.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B660-F-GAMING-WIFI-ASUS-2012.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B660-G-GAMING-WIFI-ASUS-2012.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B660-I-GAMING-WIFI-ASUS-2012.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B760-A-GAMING-WIFI-D4-ASUS-0807.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B760-F-GAMING-WIFI-ASUS-0811.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B760-G-GAMING-WIFI-D4-ASUS-0808.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B760-I-GAMING-WIFI-ASUS-0808.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-TRX40-E-GAMING-ASUS-1502.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-TRX40-XE-GAMING-ASUS-1502.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-X370-F-GAMING-ASUS-5606.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-X370-I-GAMING-ASUS-5606.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-X399-E-GAMING-ASUS-1206.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-X470-F-GAMING-ASUS-5861.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-X470-I-GAMING-ASUS-4603.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-X570-E-GAMING-ASUS-4021.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-X570-E-GAMING-WIFI-II-ASUS-4204.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-X570-E-GAMING-WIFI-II-ASUS-4404.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-X570-F-GAMING-ASUS-4021.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-X570-I-GAMING-ASUS-4021.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-X670E-A-GAMING-WIFI-ASUS-0705.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-X670E-A-GAMING-WIFI-ASUS-0805.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-X670E-E-GAMING-WIFI-ASUS-0705.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-X670E-E-GAMING-WIFI-ASUS-0805.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-X670E-F-GAMING-WIFI-ASUS-0705.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-X670E-F-GAMING-WIFI-ASUS-0805.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-X670E-I-GAMING-WIFI-ASUS-0804.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-X670E-I-GAMING-WIFI-ASUS-0822.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-Z370-E-GAMING-ASUS-3005.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-Z370-G-GAMING-ASUS-3004.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-Z370-H-GAMING-ASUS-2701.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-Z390-E-GAMING-ASUS-2004.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-Z390-F-GAMING-ASUS-2004.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-Z390-H-GAMING-ASUS-3006.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-Z390-I-GAMING-ASUS-3006.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-Z490-A-GAMING-ASUS-2403.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-Z490-E-GAMING-ASUS-2403.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-Z490-F-GAMING-ASUS-2403.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-Z490-F-GAMING-ASUS-2601.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-Z490-G-GAMING-ASUS-2403.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-Z490-G-GAMING-WIFI-ASUS-2403.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-Z490-H-GAMING-ASUS-2403.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-Z490-I-GAMING-ASUS-2403.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-Z590-A-GAMING-WIFI-ASUS-1701.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-Z590-A-GAMING-WIFI-II-ASUS-1402.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-Z590-A-GAMING-WIFI-II-ASUS-1701.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-Z590-E-GAMING-WIFI-ASUS-1701.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-Z590-F-GAMING-WIFI-ASUS-1701.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-Z590-I-GAMING-WIFI-ASUS-1701.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-ZENITH-EXTREME-ALPHA-ASUS-2202.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-ZENITH-EXTREME-ASUS-2201.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-ZENITH-II-EXTREME-ALPHA-ASUS-1603.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-ZENITH-II-EXTREME-ASUS-1603.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/STRIX-Z270E-GAMING-ASUS-1501.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/STRIX-Z270F-GAMING-ASUS-1501.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/STRIX-Z270G-GAMING-ASUS-1501.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/STRIX-Z270H-GAMING-ASUS-1501.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/STRIX-Z270I-GAMING-ASUS-2001.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-B350M-PLUS-GAMING-ASUS-6061.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-B450-PLUS-GAMING-ASUS-3802.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-A520M-PLUS-ASUS-3001.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-A520M-PLUS-II-ASUS-3001.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-A520M-PLUS-WIFI-ASUS-3001.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-B450-PLUS-II-ASUS-3802.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-B550M-E-ASUS-2803.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-B550M-E-WIFI-ASUS-2803.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-B550M-PLUS-ASUS-2803.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-B550M-PLUS-WIFI-ASUS-2803.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-B550M-PLUS-WIFI-II-ASUS-2803.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-B550-PLUS-ASUS-2803.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-B550-PLUS-WIFI-II-ASUS-2803.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-B550-PRO-ASUS-2803.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-B650M-PLUS-ASUS-0823.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-B650M-PLUS-WIFI-ASUS-0823.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-B650-PLUS-ASUS-0823.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-B650-PLUS-WIFI-ASUS-0823.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-B660M-E-D4-ASUS-2212.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-B660M-PLUS-WIFI-ASUS-2012.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-B660-PLUS-WIFI-D4-ASUS-2212.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-B760M-PLUS-D4-ASUS-0807.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-B760M-PLUS-WIFI-D4-ASUS-0807.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-B760-PLUS-WIFI-D4-ASUS-0808.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-X570-PLUS-ASUS-4021.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-X570-PLUS-WIFI-ASUS-4403.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-X570-PRO-WIFI-SI-4403.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-X670E-PLUS-ASUS-0821.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-X670E-PLUS-WIFI-ASUS-0821.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-Z490-PLUS-ASUS-2601.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-Z490-PLUS-WIFI-ASUS-2602.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-Z590-PLUS-ASUS-1801.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-Z590-PLUS-WIFI-ASUS-1601.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-Z590-PLUS-WIFI-ASUS-1801.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-Z270-MARK-1-ASUS-1501.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/Z490-GUNDAM-WIFI-ASUS-2601.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/Z590-WIFI-GUNDAM-EDITION-ASUS-1801.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/LGA1150/B85M-GAMER/B85M-GAMER-ASUS-0605.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/LGA1150/B85-PRO_GAMER/B85-PRO-GAMER-ASUS-2203.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/LGA1150/H81-GAMER/H81-GAMER-ASUS-0505.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/LGA1150/H97-PRO_GAMER/H97-PRO-GAMER-ASUS-2503.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/LGA1150/MAXIMUS-VII-HERO/MAXIMUS-VII-HERO-ASUS-3201.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/LGA1150/Z97-PRO_GAMER/Z97-PRO-GAMER-ASUS-2203.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/LGA1151/B150I_PRO_GAMING_AURA/B150I-PRO-GAMING-AURA-ASUS-2606.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/LGA1151/B150I_PRO_GAMING_WIFI_AURA/B150I-PRO-GAMING-WIFI-AURA-ASUS-2606.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/LGA1151/B150M_PRO_GAMING/B150M-PRO-GAMING-ASUS-1006.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/LGA1151/B150_PRO_GAMING_AURA/B150-PRO-GAMING-AURA-ASUS-3805.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/LGA1151/B150_PRO_GAMING/B150-PRO-GAMING-ASUS-3805.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/LGA1151/B150_PRO_GAMING_D3/B150-PRO-GAMING-D3-ASUS-2604.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/LGA1151/H170_PRO_GAMING/H170-PRO-GAMING-ASUS-3805.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/LGA1151/MAXIMUS_IX_APEX/MAXIMUS-IX-APEX-ASUS-1301.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/LGA1151/PRIME_Z270-A/PRIME-Z270-A-ASUS-1302.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/LGA1151/PRIME_Z270-K/PRIME-Z270-K-ASUS-1207.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/LGA1151/Z170-DELUXE/Z170-DELUXE-ASUS-3801.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/LGA1151/Z170I_PRO_GAMING/Z170I-PRO-GAMING-ASUS-3805.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/LGA1151/Z170_PRO_GAMING_AURA/Z170-PRO-GAMING-AURA-ASUS-3805.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/LGA1151/Z170-PRO-GAMING/Z170-PRO-GAMING-ASUS-3805.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/socket1151/Z270-WS/BIOS/Z270-WS-ASUS-0801.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/Socket2011-R3/X99-E-10G_WS/BIOS/X99-E-10G-WS-ASUS-1201.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/SocketAM3+/970_PRO_GAMING_AURA/970-PRO-GAMING-AURA-ASUS-1001.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/SocketFM2/A68HM-K/A68HM-K-ASUS-2012.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/SocketFM2/A68HM-PLUS/A68HM-PLUS-ASUS-2011.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/SocketFM2/A88X-GAMER/A88X-GAMER-ASUS-1603.zip
do
    wget -cv $bios_file || exit
done

cd ..
mkdir -p GIGABYTE
cd GIGABYTE
# download uefi firmwares
for bios_file in \
    https://download.gigabyte.com/FileList/BIOS/mb_bios_x570-aorus-elite_f37.zip \
    https://download.gigabyte.com/FileList/BIOS/mb_bios_x570-aorus-elite-wifi_f37.zip \
    https://download.gigabyte.com/FileList/BIOS/mb_bios_x570-i-aorus-pro-wifi_f36d.zip \
    https://download.gigabyte.com/FileList/BIOS/mb_bios_z690m-aorus-elite-ax-ddr4_f21.zip
do
    wget -cv $bios_file || exit
done
