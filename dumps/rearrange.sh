#!/bin/bash
# create subdirs
for dirname in `ls *.aml | sed 's|\.|\t|g' | awk '{print $1}' | sort -u`
do
	mkdir -p "${dirname}" | exit
	mv ${dirname}*.aml "${dirname}" | exit
	# convert to dsl
	find ${dirname}/*.aml | awk '{print "iasl -dl " $1}' | sh - || exit
done
