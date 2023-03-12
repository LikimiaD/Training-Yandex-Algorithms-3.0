N , M = list(map(int, input().rstrip('\n').split(' ')))
N += 1
M += 1

MATRIX = [[0] * (N) for _ in range(M)]

MATRIX[1][1] = 1

for x in range(2, M):
    for y in range(2, N):
        MATRIX[x][y] = MATRIX[x-1][y-2] + MATRIX[x-2][y-1]

print(MATRIX[-1][-1])
