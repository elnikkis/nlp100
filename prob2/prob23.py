# coding: utf-8

import sys
import re

for line in sys.stdin:
    m = re.match(r'^(=+)(.*)(=+)$', line.strip())
    print(m.group(1).split('|')[0])
    pass
