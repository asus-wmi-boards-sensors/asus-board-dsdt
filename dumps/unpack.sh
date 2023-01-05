#!/bin/bash

PWDDIR=`pwd`
PATH=$PATH:${PWDDIR}/../bin/
echo ${PATH}
mkdir -p /tmp/unpack
#ASUS
ls -1 ASUS | grep -i "\.zip" |  awk '{print "cp -v ASUS/" $1 " /tmp/unpack" }' | sh - || exit
cd /tmp/unpack
# unpack
for file in `ls -1 * | grep -i "\.zip"`
do
	# unpack
	unzip -o ${file} || exit
	# remove old capsules and unrequired files
	rm -rf *.exe *.EXE *CAP_output || exit
	rm -v ${file} || exit
	# unpack capsules
	ls -1 *.CAP | awk '{print  "uefi-firmware-parser --brute -e -O " $1 }' | sh -  || exit
	# move all DSDL to root directory
	grep -E "DSDT|SSDT" *CAP_output/* -R 2>&1 | sed 's|grep: ||g' | sed 's|: |\t|g' | awk '{print "file " $1}' | sh - \
		| grep "ACPI Machine Language file" | sed 's|:|\t|g' | awk '{print "md5sum " $1}' | sh - \
		| awk '{print "cp " $2 " `echo " $2 "| sed \"s|/|\\t|g\" | cut -f1 `." $1 ".aml"}' | sh - || exit
	# remove CAP_output from names
	ls -1 *CAP_output*.aml  | sed 's|\.|\t|g' | awk '{print "mv " $1 "." $2 "." $3 "." $4 " " $1 "." $3 "." $4}' | sh - || exit
	# remove capsules unpacks
	rm -rf *CAP_output || exit
	rm -rf *.CAP || exit
done
# Go back and copy results
cd ${PWDDIR} || exit
cp -v /tmp/unpack/*.aml .
rm -vrf /tmp/unpack/ || exit
#GIGABYTE
mkdir -p /tmp/unpack
ls -1 GIGABYTE | grep -i "\.zip" |  awk '{print "cp -v GIGABYTE/" $1 " /tmp/unpack" }' | sh - || exit
cd /tmp/unpack
# unpack
for file in `ls -1 *.zip`
do
	echo ${file} | sed "s|.zip||g" | awk '{print "mkdir -p " $1 "CAP_output" }' | sh -
	echo ${file} | sed "s|.zip||g" | awk '{print "unzip " $1 ".zip -d " $1 "CAP_output" }' | sh -
	# remove unrequired
	echo ${file} | sed "s|.zip||g" | awk '{print "rm -rvf " $1 "CAP_output/*.bat" }' | sh -
	echo ${file} | sed "s|.zip||g" | awk '{print "rm -rvf " $1 "CAP_output/*.exe" }' | sh -
	echo ${file} | sed "s|.zip||g" | awk '{print "rm -rvf " $1 "CAP_output/*.txt" }' | sh -
	echo ${file} | sed "s|.zip||g" | awk '{print "rm -rvf " $1 "CAP_output/EFI/" }' | sh -
	echo ${file} | sed "s|.zip||g" | awk '{print "rm -rvf " $1 "CAP_output/*.pdf" }' | sh -
	echo ${file} | sed "s|.zip||g" | awk '{print "rm -rvf " $1 "CAP_output/*.efi" }' | sh -
	echo ${file} | sed "s|.zip||g" | awk '{print "rm -rvf " $1 "CAP_output/*.nsh" }' | sh -
	# unpack
	echo ${file} | sed "s|.zip||g" \
		| awk '{print  "uefi-firmware-parser --brute -e -O " $1 "CAP_output/*" }' | sh -  || exit
	echo Proccesed ${file}
	# move all DSDL to root directory
	grep -E "DSDT|SSDT" *CAP_output/* -R 2>&1 | sed 's|grep: ||g' | sed 's|: |\t|g' | awk '{print "file " $1}' | sh - \
		| grep "ACPI Machine Language file" | sed 's|:|\t|g' | awk '{print "md5sum " $1}' | sh - \
		| awk '{print "cp " $2 " `echo " $2 "| sed \"s|/|\\t|g\" | cut -f1 `." $1 ".aml"}' | sh - || exit
	# rename without output
	ls -1 *CAP_output*.aml  | sed 's|\.|\t|g' | sed 's|CAP_output||g' \
		| sed 's|mb_bios_||g' \
		| awk '{print "mv -v mb_bios_"$1 "CAP_output." $2 ".aml " $1 "-GIGABYTE." $2 ".aml" }' | sh -
	# cleanup
	echo ${file} | sed "s|.zip||g" | awk '{print "rm -rf " $1 "CAP_output" }' | sh -
	echo ${file} | sed "s|.zip||g" | awk '{print "rm " $1 ".zip" }' | sh -
done

# Go back and copy results
cd ${PWDDIR} || exit
cp -v /tmp/unpack/*.aml .
rm -vrf /tmp/unpack/ || exit
