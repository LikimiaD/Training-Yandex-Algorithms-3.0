file = open("input.txt", "r")

N, M = map(int, file.readline().split(' '))

DICT = {x:[] for x in range(1,N+1)}

for _ in range(M):
    x,y = map(int, file.readline().split(' '))
    DICT[x].append(y)
    DICT[y].append(x)

def dfs(v, num, visited):
    visited.add(v)
    for value in DICT[v]:
        if value not in visited:
            dfs(value, num, visited)

visited = set()
num = 0
for value in range(1,N+1):
    if value not in visited:
        dfs(value, num, visited)
        num += 1

print(num)
