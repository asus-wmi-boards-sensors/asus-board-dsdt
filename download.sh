#!/bin/bash

# asus bioses
mkdir -p ASUS
cd ASUS
# download capsules
for bios_file in \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/CROSSHAIR-VI-HERO-ASUS-8601.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/MAXIMUS-IX-EXTREME-ASUS-1501.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B360-PLUS-ASUS-3101.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B450-PLUS-ASUS-3802.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B460-PLUS-ASUS-1620.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B550M-A-AC-ASUS-2803.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B550M-A-ASUS-2803.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B550M-A-WIFI-ASUS-2803.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B550M-A-WIFI-II-ASUS-2803.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B550M-K-ASUS-2803.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B550-PLUS-ASUS-2803.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B650M-A-ASUS-0812.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B650M-A-WIFI-ASUS-0812.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-B650-PLUS-ASUS-0809.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-H410M-R-ASUS-1620.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-X370-PRO-ASUS-6042.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-X399-A-ASUS-1206.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-X470-PRO-ASUS-6042.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-X570-P-ASUS-4021.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-X570-PRO-ASUS-4021.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-Z270M-PLUS-ASUS-2001.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-Z270-P-ASUS-2001.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-Z370-A-ASUS-3004.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-Z370-A-II-ASUS-3004.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ProArt-B550-CREATOR-ASUS-2803.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ProArt-B660-CREATOR-D4-ASUS-2103.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PROART-X570-CREATOR-WIFI-ASUS-0801.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ProArt-X670E-CREATOR-WIFI-ASUS-0705.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ProArt-Z490-CREATOR-10G-ASUS-2601.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ProArt-Z690-CREATOR-WIFI-ASUS-2103.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ProArt-Z790-CREATOR-WIFI-ASUS-0703.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/Pro-B550M-C-SI-2423.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/Pro-B550M-C-SI-2804.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRO-H410T-SI-1623.ZIP \
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
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-CROSSHAIR-X670E-HERO-ASUS-0705.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-MAXIMUS-X-HERO-ASUS-2701.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-MAXIMUS-XI-HERO-ASUS-2004.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-MAXIMUS-XI-HERO-WIFI-ASUS-2004.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-MAXIMUS-XIII-EXTREME-GLACIAL-ASUS-1402.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-MAXIMUS-Z690-EXTREME-ASUS-2103.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-MAXIMUS-Z690-EXTREME-GLACIAL-ASUS-2103.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-MAXIMUS-Z790-EXTREME-ASUS-0703.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B350-F-GAMING-ASUS-5606.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B350-I-GAMING-ASUS-5606.ZIP \
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
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B650E-E-GAMING-WIFI-ASUS-0804.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B650E-F-GAMING-WIFI-ASUS-0804.zip \
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
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-X670E-E-GAMING-WIFI-ASUS-0705.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-X670E-F-GAMING-WIFI-ASUS-0705.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-X670E-I-GAMING-WIFI-ASUS-0804.zip \
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
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-Z590-A-GAMING-WIFI-II-ASUS-1402.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-ZENITH-EXTREME-ALPHA-ASUS-2202.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-ZENITH-EXTREME-ASUS-2201.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-ZENITH-II-EXTREME-ALPHA-ASUS-1603.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-ZENITH-II-EXTREME-ASUS-1603.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/STRIX-Z270E-GAMING-ASUS-1501.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/STRIX-Z270F-GAMING-ASUS-1501.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/STRIX-Z270G-GAMING-ASUS-1501.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/STRIX-Z270H-GAMING-ASUS-1501.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/STRIX-Z270I-GAMING-ASUS-2001.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-B450-PLUS-GAMING-ASUS-3802.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-B450-PLUS-II-ASUS-3802.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-B550M-E-ASUS-2803.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-B550M-E-WIFI-ASUS-2803.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-B550M-PLUS-ASUS-2803.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-B550M-PLUS-WIFI-ASUS-2803.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-B550M-PLUS-WIFI-II-ASUS-2803.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-B550-PLUS-ASUS-2803.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-B550-PLUS-WIFI-II-ASUS-2803.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-B550-PRO-ASUS-2803.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-X570-PLUS-ASUS-4021.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-X570-PLUS-WIFI-ASUS-4403.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-X570-PRO-WIFI-SI-4403.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-Z490-PLUS-ASUS-2601.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-Z490-PLUS-WIFI-ASUS-2602.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-Z590-PLUS-WIFI-ASUS-1601.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-Z270-MARK-1-ASUS-1501.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/Z490-GUNDAM-WIFI-ASUS-2601.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/LGA1150/MAXIMUS-VII-HERO/MAXIMUS-VII-HERO-ASUS-3201.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/LGA1151/MAXIMUS_IX_APEX/MAXIMUS-IX-APEX-ASUS-1301.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/LGA1151/PRIME_Z270-A/PRIME-Z270-A-ASUS-1302.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/LGA1151/PRIME_Z270-K/PRIME-Z270-K-ASUS-1207.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/LGA1151/Z170-DELUXE/Z170-DELUXE-ASUS-3801.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/socket1151/Z270-WS/BIOS/Z270-WS-ASUS-0801.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/Socket2011-R3/X99-E-10G_WS/BIOS/X99-E-10G-WS-ASUS-1201.zip
do
    wget -cv $bios_file || exit
done

cd ..
mkdir -p GIGABYTE
cd GIGABYTE
# download uefi firmwares
for bios_file in \
    https://download.gigabyte.com/FileList/BIOS/mb_bios_x570-i-aorus-pro-wifi_f36d.zip
do
    wget -cv $bios_file || exit
done
