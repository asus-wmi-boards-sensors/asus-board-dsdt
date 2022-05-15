#!/bin/bash

# download capsules
for bios_file in \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRO-H410T-SI-1623.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-H410M-R-ASUS-1620.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-X570-P-ASUS-4021.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-X570-PRO-ASUS-4021.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/Pro-B550M-C-SI-2423.ZIP \
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
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B550-I-GAMING-ASUS-2423.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B550-XE-GAMING-WIFI-ASUS-2425.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-TRX40-E-GAMING-ASUS-1502.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-TRX40-XE-GAMING-ASUS-1502.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-X370-F-GAMING-ASUS-5606.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-X370-I-GAMING-ASUS-5606.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-X470-F-GAMING-ASUS-5861.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-X470-I-GAMING-ASUS-4603.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-X570-E-GAMING-ASUS-4021.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-X570-E-GAMING-WIFI-II-ASUS-4204.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-X570-F-GAMING-ASUS-4021.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-X570-I-GAMING-ASUS-4021.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-Z370-G-GAMING-ASUS-3004.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-Z370-H-GAMING-ASUS-2701.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-Z390-E-GAMING-ASUS-2004.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-Z390-F-GAMING-ASUS-2004.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-Z390-H-GAMING-ASUS-3006.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-Z390-I-GAMING-ASUS-3006.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-Z490-A-GAMING-ASUS-2403.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-Z490-E-GAMING-ASUS-2403.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-Z490-F-GAMING-ASUS-2403.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-Z490-G-GAMING-ASUS-2403.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-Z490-G-GAMING-WIFI-ASUS-2403.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-Z490-H-GAMING-ASUS-2403.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-Z490-I-GAMING-ASUS-2403.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-X570-PLUS-ASUS-4021.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/LGA1150/MAXIMUS-VII-HERO/MAXIMUS-VII-HERO-ASUS-3201.zip \
    https://dlcdnets.asus.com/pub/ASUS/mb/LGA1151/Z170-DELUXE/Z170-DELUXE-ASUS-3801.zip
do
    wget -cv $bios_file || exit
done
