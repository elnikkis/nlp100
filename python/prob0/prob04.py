# coding: utf-8

s = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
words = [token.strip(',.') for token in s.split()]

fst_idx = {1, 5, 6, 7, 8, 9, 15, 16, 19}
d = {}
for i, word in enumerate(words):
    if i+1 in fst_idx:
        d[word[0]] = i + 1
    else:
        d[word[0:2]] = i + 1
print(sorted(d.items(), key=lambda x: x[1]))

