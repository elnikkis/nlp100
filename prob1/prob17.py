
import sys
import csv

uniq = {line[0] for line in csv.reader(sys.stdin, delimiter='\t')}

for a in uniq:
    print(a)
