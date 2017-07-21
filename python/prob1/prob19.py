# coding: utf-8

import sys
import csv
from collections import Counter

col1 = [line[0] for line in csv.reader(sys.stdin, delimiter='\t')]
counter = Counter(col1)

for s in counter.most_common():
    print(*s, sep='\t')
