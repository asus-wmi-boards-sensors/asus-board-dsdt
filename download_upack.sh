# download capsules
for bios_file in \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-X570-P-ASUS-4021.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/PRIME-X570-PRO-ASUS-4021.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/Pro-B550M-C-SI-2423.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B550-A-GAMING-ASUS-2423.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B550-E-GAMING-ASUS-2423.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B550-F-GAMING-ASUS-2423.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B550-F-GAMING-WIFI-ASUS-2423.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B550-F-GAMING-WIFI-II-ASUS-0305.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B550-I-GAMING-ASUS-2423.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-B550-XE-GAMING-WIFI-ASUS-2425.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-X570-E-GAMING-ASUS-4021.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-X570-F-GAMING-ASUS-4021.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-X570-I-GAMING-ASUS-4021.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-Z390-E-GAMING-ASUS-2004.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-Z390-F-GAMING-ASUS-2004.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-Z390-H-GAMING-ASUS-3006.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/ROG-STRIX-Z390-I-GAMING-ASUS-3006.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/BIOS/TUF-GAMING-X570-PLUS-ASUS-4021.ZIP \
    https://dlcdnets.asus.com/pub/ASUS/mb/LGA1150/MAXIMUS-VII-HERO/MAXIMUS-VII-HERO-ASUS-3201.zip # Use some different capsule format/ can get DSDT from it
do
    wget -cv $bios_file || exit
done

# unpack
ls -1 *.ZIP | awk '{print "unzip -u " $1 }' || exit
# remove old capsules and unrequired files
rm -rf *.exe *CAP_output *.dsl *.aml || exit
# unpack capsules
ls -1 *.CAP | awk '{print  "../bin/uefi-firmware-parser --brute -e -O " $1 }' | sh -  || exit
# move all DSDL to root directory
grep ALASKA * -R 2>&1 | sed 's|grep: ||g' | sed 's|: |\t|g' | awk '{print "file " $1}' | sh - | grep DSDT | sed 's|:|\t|g' | awk '{print "md5sum " $1}' | sh - | sed 's|/|\t|g' | awk '{print "cp -v " $2 "/" $3 "/" $4 "/" $5 "/" $6 "/" $7 "/" $8 "/" $9 " " $2 "." $1 ".aml" }' | sh - || exit
# remove CAP_output from names
ls -1 *.aml  | sed 's|\.|\t|g' | awk '{print "mv " $1 "." $2 "." $3 "." $4 " " $1 "." $3 "." $4}' | sh - || exit
# remove capsules unpacks
rm -rf *CAP_output || exit
# convert to dsl
ls -1 *.aml | awk '{print "iasl -d " $1}' | sh - || exit
