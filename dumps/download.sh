#!/bin/bash

# asus bioses
mkdir -p ASUS
cd ASUS
# download capsules
for bios_file in \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ProArt-Z690-CREATOR-WIFI-ASUS-2103.zip
do
    wget -cv $bios_file || exit
done

cd ..
mkdir -p GIGABYTE
cd GIGABYTE
# download uefi firmwares
for bios_file in \
    https://download.gigabyte.com/FileList/BIOS/mb_bios_z690m-aorus-elite-ax-ddr4_f21.zip
do
    wget -cv $bios_file || exit
done
