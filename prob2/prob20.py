# coding: utf-8

# gzip -dc jawiki-country.json.gz | python prob20.py > uk.txt

import sys
import gzip
import json

for line in sys.stdin:
    kiji = json.loads(line)
    if kiji['title'] == 'イギリス':
        print(kiji['text'])
