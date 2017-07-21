# coding: utf-8

import sys
import re

# less uk.txt | grep -e '^=' | python prob23.py

for line in sys.stdin:
    m = re.match(r'^(=+)(.*)(\1)$', line.strip())
    section_tag = m.group(1).split('|')[0]
    level = len(section_tag) - 1
    print(m.group(2), level)
