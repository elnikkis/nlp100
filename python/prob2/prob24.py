# coding: utf-8

import sys
import re

# less uk.txt | python prob24.py

for line in sys.stdin:
    m = re.match(r'(\[\[File|ファイル):([^|\]]*)', line.strip())
    if m:
        print(m.group(2))
