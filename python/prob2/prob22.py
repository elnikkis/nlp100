# coding: utf-8

import sys
import re

# Usage: bash prob21.sh | python prob22.py
# [[Category:英連邦王国|*]]

for line in sys.stdin:
    m = re.match(r'^\[\[Category:(.*)\]\]$', line.strip())
    print(m.group(1).split('|')[0])
    pass
