STACK_FIRST = list("1 3 5 7 9".split(' '))
STACK_SECOND = list("2 4 6 8 0".split(' '))

count = 0

while(len(STACK_FIRST) != 0 or len(STACK_SECOND) != 0):
    x = STACK_FIRST[0]
    y = STACK_SECOND[0]
    if (x  > y):
        STACK_SECOND.remove(y)
        STACK_FIRST.remove(x)
        STACK_FIRST.append(x)
        STACK_FIRST.append(y)
    else:
        STACK_SECOND.remove(y)
        STACK_FIRST.remove(x)
        STACK_SECOND.append(x)
        STACK_SECOND.append(y)
    count += 1