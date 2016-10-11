# coding: utf-8

import sys
import re

# [[Category:英連邦王国|*]]

for line in sys.stdin:
    m = re.match('^\[\[Category:(.*)(\|.*)?\]\]$', line.strip())
    print(m.group(1))
    print(m.groups)
    pass
