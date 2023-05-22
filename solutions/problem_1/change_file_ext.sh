#!/bin/bash

dir=$1
from=$2
to=$3

cnt=0

for i in "$dir/"*."$from"; do
  mv -- "$i" "${i%.$from}.$to";
  ((cnt+=1))
done

echo "Changed extension of $cnt files from (.$from to .$to)."
echo "Done."