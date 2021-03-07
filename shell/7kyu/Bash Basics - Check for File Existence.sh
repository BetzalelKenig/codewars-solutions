# Write a BASH script which checks for a given file. If the file exists, print "Found *fileName*" to stdout, otherwise print "Can't find *fileName*."

# If no arguments are supplied, print "Nothing to find"

# Examples:

# file exists: 
# run_shell file1.txt --> "Found file1.txt"

# file doesn't exist:
# run_shell file1.txt --> "Can't find file1.txt"

# No arguments:
# run_shell --> "Nothing to find"
# Please note: the locate command is unavailable on Codewars.

#!/bin/bash

if [ ${#} == 0 ]
then
  echo "Nothing to find"
elif [ -f $1 ]
then
  echo "Found $1"
else
  echo "Can't find $1"
fi