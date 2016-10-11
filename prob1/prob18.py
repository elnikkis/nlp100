# coding: utf-8

import sys
import csv

data = [line for line in csv.reader(sys.stdin, delimiter="\t")]

so = sorted(data, key=lambda x: float(x[2]), reverse=True)

for line in so:
    print(*line, sep='\t')
