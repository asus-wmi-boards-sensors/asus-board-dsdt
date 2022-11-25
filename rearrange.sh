#!/bin/bash
# create subdirs
for dirname in `ls *.aml | sed 's|\.|\t|g' | awk '{print $1}' | sort -u`
do
	mkdir -p "${dirname}" | exit
	mv ${dirname}*.aml "${dirname}" | exit
done
# convert to dsl
find * | grep "\.aml" | awk '{print "iasl -d " $1}' | sh - || exit
