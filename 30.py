file = open('input.txt', 'r')

N_1 =  int(file.readline().rstrip())
TEXT_1 = list(map(int, file.readline().rsplit()))

N_2 =  int(file.readline().rstrip())
TEXT_2 = list(map(int, file.readline().rsplit()))


L = [[0] * (N_2+1) for _ in range(N_1+1)]
for x in range(1, N_1+1):
    for y in range(1, N_2+1):
        if TEXT_1[x-1] == TEXT_2[y-1]:
            L[x][y] = 1 + L[x-1][y-1]
        else:
            L[x][y] = max(L[x-1][y], L[x][y-1])

lcs = []
i, j = N_1, N_2
while i > 0 and j > 0:
    if TEXT_1[i - 1] == TEXT_2[j - 1]:
        lcs.append(TEXT_1[i - 1])
        i -= 1
        j -= 1
    elif L[i - 1][j] > L[i][j - 1]:
        i -= 1
    else:
        j -= 1

print(*reversed(lcs))