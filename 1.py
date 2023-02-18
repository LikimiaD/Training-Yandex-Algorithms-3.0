f = open('input.txt', 'r')

x = f.read().replace(' ', '').rstrip('\n').replace('\n', '')

DICT = {}
for symbol in set(x):
    DICT[symbol] = 0
for symbol in x:
    DICT[symbol] += 1
LIST = list(sorted(set(x)))
for num in range(max(DICT.values()),0, -1):
    z = ''
    for symbol in LIST:
        if (DICT[symbol] >= num): z += '#'
        else: z += ' '
    print(z)
print(''.join(LIST))