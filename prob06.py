# coding: utf-8

from prob05 import ngram

s1 = 'paraparaparadise'
s2 = 'paragraph'

X = set(ngram(s1))
Y = set(ngram(s2))

print(X | Y)
print(X & Y)
print(X - Y)

if ('s', 'e') in X:
    print('"se" in X')
else:
    print('"se" not in X')

if ('s', 'e') in Y:
    print('"se" in Y')
else:
    print('"se" not in Y')
