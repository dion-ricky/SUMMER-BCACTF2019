#!/usr/bin/env python3

one = open('one.txt', 'r').read()
two = open('two.txt', 'r').read()

_one = one.split(' ')
_two = two.split(' ')

flag = []

for i in range(len(_one)):
    _a = int(_one[i], 16)
    _b = int(_two[i], 16)
    flag.append(chr(_a + _b))

print(''.join(flag))
