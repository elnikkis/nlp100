# coding: utf-8

def cipher(s):
    ciphed = []
    for c in s:
        if c.islower():
            c = chr(219 - ord(c))
        ciphed.append(c)
    return ''.join(ciphed)

cy = cipher('Hello world!')
print(cy)

print(cipher(cy))

