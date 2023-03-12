from collections import deque

file = open("input.txt", "r")

N, M = map(int, file.readline().split(' '))

DICT = {x:[] for x in range(1,N+1)}

for _ in range(M):
    x,y = map(int, file.readline().split(' '))
    DICT[x].append(y)
    DICT[y].append(x)

visited = {key:False for key in DICT.keys()}

def bfs(graph, visited, start):
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

bfs(DICT, visited, 1)

trash = [value for value in visited.keys() if visited[value] == True]
print(len(trash))
print(*trash)