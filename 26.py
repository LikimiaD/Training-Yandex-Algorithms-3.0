file = open('input.txt', 'r')
mainN, secondN = map(int, file.readline().split())
LIST = [[float('Inf')] + list(map(int, file.readline().rstrip('\n').split(' '))) if _ != 0 else [float('Inf')] * (secondN + 1) for _ in range(0, mainN+ 1)]
file.close()

for i in range(1,mainN+1):
    for j in range(1, secondN + 1):
        if i == 1 and j == 1:
            pass
        else:
            LIST[i][j] = min(LIST[i-1][j], LIST[i][j-1]) + LIST[i][j]

print(LIST[-1][-1])

