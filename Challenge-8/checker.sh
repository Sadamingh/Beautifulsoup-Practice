#!/bin/bash/

python *.py > /tmp/output.txt

file1=$(cat output.txt)
file2=$(cat /tmp/output.txt)

if [ "$file1" = "$file2" ]
then
    echo "All Tests Pass"
else
    echo "Failed Test"
fi
