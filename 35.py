file = open("input.txt", "r")

N = int(file.readline())

DICT = {x:[] for x in range(1,N+1)}

for _ in range(1,N+1):
    text = list(map(int, file.readline().rstrip().split(' ')))
    for num in range(N):
        if text[num]:
            DICT[_].append(num+1)

def dfs(v, num, visited):
    visited.append(v)
    for value in DICT[v]:
        if value not in visited:
            dfs(value, num, visited)

visited = list()
num = 0
for value in range(1,N+1):
    if value not in visited:
        dfs(value, num, visited)
        num += 1

print(num)
