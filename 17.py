STACK_FIRST = list("2 4 6 8 0".split(' '))
STACK_SECOND = list("1 3 5 7 9".split(' '))

count = 0

while (len(STACK_FIRST) > 0 or len(STACK_SECOND) > 0):
    first = STACK_FIRST[0]
    second = STACK_SECOND[0]
    STACK_FIRST.remove(first)
    STACK_SECOND.remove(second)
    if (first == 0 and second == 9):
        STACK_SECOND.append(first)
        STACK_SECOND.append(second)
    elif (first == 9 and second == 0):
        STACK_FIRST.append(first)
        STACK_FIRST.append(second)
    elif (first < second):
        STACK_FIRST.append(first)
        STACK_FIRST.append(second)
    else:
        STACK_SECOND.append(first)
        STACK_SECOND.append(second)
    count += 1

print(f"second {count}" if len(STACK_SECOND) == 0 else f"first {count}")