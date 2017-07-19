# -*- coding: utf-8 -*-

import sys
import re


with open('uk.txt', 'r') as fp:
    uk_text = fp.read()

#m = re.search(r'\{\{基礎情報(.*?)\}\}', uk_text, re.DOTALL)
#print(m.group(0))

def parse_template(text):
    info = []
    flag = False
    for line in text.split('\n'):
        if line.startswith('{{基礎情報'):
            flag = True
            continue
        elif line.startswith('}}'):
            flag = False
        if flag:
            info.append(line)
    return '\n'.join(info)


def parse_attr(text):
    results = {'field': [], 'value': []}
    token = []
    def Field(s, token, results):
        if s != '=':
            token.append(s)
            return Field
        else:
            results['field'].append(''.join(token).strip())
            token.clear()
            return Value

    def Value(s, token, results):
        #print(getattr(Value, 'open', 0))
        if s != '|' or (s == '|' and getattr(Value, 'open', 0) > 0):
            if s == '{' or s == '[':
                Value.open = getattr(Value, 'open', 0) + 1
            elif s == '}' or s == ']':
                Value.open = getattr(Value, 'open', 0) - 1
            token.append(s)
            return Value
        else:
            results['value'].append(''.join(token).strip())
            token.clear()
            return Field

    state = Field
    for s in text[1:]:
        state = state(s, token, results)

    results['value'].append(''.join(token).strip())
    return results

def test():
    results = re.finditer(r'\|([^|]*)', text, re.DOTALL)
    for result in results:
        yield result.group()

a = parse_template(uk_text)
#print(a)
b = parse_attr(a)
#print(b)

assert len(b['field']) == len(b['value'])
d = {k:v for k, v in zip(b['field'], b['value'])}

for k, v in d.items():
    print(k, '::', v.replace('\n', '\\n'))
