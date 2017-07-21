# coding: utf-8

x = input('x=')
y = input('y=')
z = input('z=')

def what_time(x, y, z):
    return '{}時の{}は{}'.format(x, y, z)

print(what_time(x, y, z))
