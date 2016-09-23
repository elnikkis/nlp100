# coding: utf-8

s = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

tokens = s.split()
words = [token.strip(',.') for token in tokens]
counts = [len(w) for w in words]
print(counts)
