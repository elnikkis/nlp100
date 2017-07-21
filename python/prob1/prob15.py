# coding: utf-8


N = int(input('N='))

with open('hightemp.txt', 'r') as fp:
    lines = fp.readlines()
    print(''.join(lines[-N:]), end='')


# tail hightemp.txt
