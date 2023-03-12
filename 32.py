from collections import deque

file = open("input.txt", "r")

N, M = map(int, file.readline().split(' '))

DICT = {x:[] for x in range(1,N+1)}

for _ in range(M):
    x,y = map(int, file.readline().split(' '))
    DICT[x].append(y)
    DICT[y].append(x)

def dfs(v, num, visited, points):
    stack = deque([v])
    while stack:
        current = stack.pop()
        visited.add(current)
        points[current] = True
        for neighbor in DICT[current]:
            if neighbor not in visited:
                stack.append(neighbor)

visited = set()
num = 0
ANSWER = {}
for value in range(1,N+1):
    if value not in visited:
        points = {key:False for key in DICT.keys()}
        dfs(value, num, visited, points)
        ANSWER[num] = [key for key, value in points.items() if value == True]
        num += 1

print(num)
for value in ANSWER.values():
    print(len(value))
    print(*value) 
