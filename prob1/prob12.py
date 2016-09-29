# coding: utf-8

import sys
import csv

with open('col1.txt', 'w') as fp1, open('col2.txt', 'w') as fp2:
    for line in csv.reader(sys.stdin, delimiter='\t'):
        print(line[0], file=fp1)
        print(line[1], file=fp2)
