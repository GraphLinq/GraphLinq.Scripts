#!/bin/bash

FILE=nodes.csv
if test -f "$FILE"; then
    echo "$FILE exists."
    rm nodes.csv
fi

wget https://raw.githubusercontent.com/GraphLinq/GraphLinq.IDE/master/js/node_schema.json

python3 export.py

rm -f node_schema.json

