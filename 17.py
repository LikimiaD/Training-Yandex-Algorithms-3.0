list_first = list(map(int,input().rstrip('\n').split()))
list_second = list(map(int,input().rstrip('\n').split()))

count = 0

while (list_first and list_second):
    if count >= 10**6:
        break
    first = list_first[0]
    list_first.remove(first)
    second = list_second[0]
    list_second.remove(second)
    count += 1
    if (first == 0 and second == 9):
        list_first.append(first)
        list_first.append(second)
    elif (first == 9 and second == 0):
        list_second.append(first)
        list_second.append(second)
    elif (first < second):
        list_second.append(first)
        list_second.append(second)
    elif (first > second):
        list_first.append(first)
        list_first.append(second)
    else:
        pass

if (count >= 10**6):
    print('botva')
else:
    print(f"second {count}" if len(list_first) == 0 else f"first {count}")