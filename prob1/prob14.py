# coding: utf-8

import sys

N = int(input('N='))

with open('hightemp.txt', 'r') as fp:
    for i, line in zip(range(N), fp):
        print(line, end='')
