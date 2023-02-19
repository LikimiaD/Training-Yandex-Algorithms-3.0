f = open('input.txt', 'r')
M = int(f.readline())
LIST = []
for _ in range(int(f.readline())):
    if not (len(LIST)):
        x = list(f.readline().split())
        if ( 1 <= int(x[0]) <= int(x[1]) <= M):
            LIST.append(x)
    else:
        x = list(f.readline().split())
        if ( 1 <= int(x[0]) <= int(x[1]) <= M):
            TRASH = []
            for value in LIST:
                if not int(value[0]) <= int(x[1]) or int(x[0]) <= int(value[1]):
                    TRASH.append(value)
            for value in TRASH:
                LIST.remove(value)
            LIST.append(x)
print(len(LIST))