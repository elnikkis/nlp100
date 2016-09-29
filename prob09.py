# coding: utf-8

import random

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

def typoglycemia(s):
    result = []
    for token in s.split():
        if len(token) > 4:
            tmp = list(token[1:-1])
            random.shuffle(tmp)
            token = token[0] + ''.join(tmp) + token[-1]
        result.append(token)
    return ' '.join(result)

print(s)
print(typoglycemia(s))
