#!/bin/bash

cat "" > res_curl.txt
i=1
while [ $i -le 500 ]
do
	echo "iteration $i"
	curl http://localhost:83 >> res_curl.txt
	((i++))
done

cat res_curl.txt | grep "Hello 1" | wc -l
cat res_curl.txt | grep "Hello 2" | wc -l