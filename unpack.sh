#!/bin/bash

# unpack
ls -1 | grep -i "\.zip" |  awk '{print "unzip -o " $1 }' | sh -
# remove old capsules and unrequired files
rm -rf *.exe *.EXE *CAP_output *.dsl || exit
# unpack capsules
ls -1 *.CAP | awk '{print  "../bin/uefi-firmware-parser --brute -e -O " $1 }' | sh -  || exit
# move all DSDL to root directory
grep ALASKA *CAP_output/* -R 2>&1 | sed 's|grep: ||g' | sed 's|: |\t|g' | awk '{print "file " $1}' | sh - | grep DSDT | sed 's|:|\t|g' | awk '{print "md5sum " $1}' | sh - | sed 's|/|\t|g' | awk '{print "cp -v " $2 "/" $3 "/" $4 "/" $5 "/" $6 "/" $7 "/" $8 "/" $9 " " $2 "." $1 ".aml" }' | sh - || exit
# remove CAP_output from names
ls -1 *CAP_output*.aml  | sed 's|\.|\t|g' | awk '{print "mv " $1 "." $2 "." $3 "." $4 " " $1 "." $3 "." $4}' | sh - || exit
# remove capsules unpacks
rm -rf *CAP_output || exit
# convert to dsl
ls -1 *.aml | awk '{print "iasl -d " $1}' | sh - || exit

