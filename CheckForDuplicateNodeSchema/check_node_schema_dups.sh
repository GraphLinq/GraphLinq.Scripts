#!/bin/bash

wget https://raw.githubusercontent.com/GraphLinq/GraphLinq.IDE/master/js/node_schema.json

python3 duplicates.py

rm -f node_schema.json

