maxVal = int(input())
LIST = []
for i in range(int(input())):
    if LIST == []:
        LIST.append(list(map(int, input().split(' '))))
    else:
        a,b = list(map(int, input().split(' ')))
        for value in LIST:
            c,d = value
            if (a <= d) and (c <= b):
                LIST.remove(value)
        LIST.append([a,b])

print(LIST)
print(len(LIST))