#!/bin/bash

PWDDIR=`pwd`
PATH=$PATH:${PWDDIR}/../bin/
echo ${PATH}
mkdir -p /tmp/unpack
#ASUS
ls -1 ASUS | grep -i "\.zip" |  awk '{print "cp -v ASUS/" $1 " /tmp/unpack" }' | sh - || exit
cd /tmp/unpack
# unpack
ls -1 | grep -i "\.zip" |  awk '{print "unzip -o " $1 }' | sh - || exit
# remove old capsules and unrequired files
rm -rf *.exe *.EXE *CAP_output *.dsl */*.dsl || exit
ls -1 | grep -i "\.zip" |  awk '{print "rm -v " $1 }' | sh - || exit
# unpack capsules
ls -1 *.CAP | awk '{print  "uefi-firmware-parser --brute -e -O " $1 }' | sh -  || exit
# move all DSDL to root directory
grep ALASKA *CAP_output/* -R 2>&1 | sed 's|grep: ||g' | sed 's|: |\t|g' | awk '{print "file " $1}' | sh - \
	| grep "ACPI Machine Language file" | sed 's|:|\t|g' | awk '{print "md5sum " $1}' | sh - \
	| awk '{print "cp " $2 " `echo " $2 "| sed \"s|/|\\t|g\" | cut -f1 `." $1 ".aml"}' | sh - || exit
# remove CAP_output from names
ls -1 *CAP_output*.aml  | sed 's|\.|\t|g' | awk '{print "mv " $1 "." $2 "." $3 "." $4 " " $1 "." $3 "." $4}' | sh - || exit
# remove capsules unpacks
rm -rf *CAP_output || exit
rm -rf *.CAP || exit
# Go back and copy results
cd ${PWDDIR} || exit
cp -v /tmp/unpack/*.aml .
rm -vrf /tmp/unpack/ || exit
ls -1 | grep -i "\.zip" |  awk '{print "rm -v " $1 }' | sh - || exit
# create subdirs
for dirname in \
	"CROSSHAIR" \
	"MAXIMUS" \
	"PRIME-B450" \
	"PRIME-B550" \
	"PRIME-B650" \
	"PRIME-H410" \
	"PRIME-X370" \
	"PRIME-X470" \
	"PRIME-X570" \
	"PRIME-Z270" \
	"ProArt" \
	"Pro-WS-X570" \
	"ROG-CROSSHAIR" \
	"ROG-MAXIMUS" \
	"ROG-STRIX-B350" \
	"ROG-STRIX-B450" \
	"ROG-STRIX-B550" \
	"ROG-STRIX-B650" \
	"ROG-STRIX-X370" \
	"ROG-STRIX-X470" \
	"ROG-STRIX-X570" \
	"ROG-STRIX-X670" \
	"ROG-STRIX-Z370" \
	"ROG-STRIX-Z390" \
	"ROG-STRIX-Z490" \
	"ROG-STRIX-Z590" \
	"ROG-STRIX-Z690" \
	"STRIX-Z270" \
	"TUF-B450" \
	"TUF-GAMING-B450" \
	"TUF-GAMING-B550" \
	"TUF-GAMING-X570"
do
	mkdir -p ${dirname}
	mv ${dirname}*.aml ${dirname}
done
# convert to dsl
find * | grep "\.aml" | awk '{print "iasl -d " $1}' | sh - || exit

