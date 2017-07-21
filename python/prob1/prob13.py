# coding: utf-8

with open('col1.txt', 'r') as fp1, open('col2.txt', 'r') as fp2:
    for l1, l2 in zip(fp1, fp2):
        print(l1.rstrip(), l2.rstrip(), sep='\t')
