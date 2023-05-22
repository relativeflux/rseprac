#!/bin/bash

dir=$1
num_values=$2

num_defective_files=0

for i in "$dir/"*; do
  cnt=$(wc -w < "$i")
  if [ "$cnt" -lt "$num_values" ]
  then
    echo "File $i contains $cnt values."
    ((num_defective_files+=1))
  fi
done

if [ "$num_defective_files" -gt 0 ]
then
  echo "WARNING: $num_defective_files files containing fewer than $num_values values were detected."
else
  echo "All sample files OK."
fi

echo "Done."