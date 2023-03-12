from collections import deque

file = open("input.txt", "r")

N = int(file.readline().rstrip())

DICT = {key : [] for key in range(1,N+1)}

for _ in range(1,N+1):
    text = list(map(int, file.readline().rstrip().split(' ')))
    for num in range(N):
        if text[num]:
            DICT[_].append(num+1)

start, end = map(int, file.readline().rstrip().split(' '))

visited = {key:False for key in DICT.keys()}

STACK = []

def bfs(graph, visited, start, end):
    queue = deque([(start, 0, [start])])
    visited[start] = True
    while queue:
        node, steps, path = queue.popleft()
        if node == end:
            return steps, path
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, steps + 1, path + [neighbor]))
    return -1

x = bfs(DICT, visited, start, end)
if (type(x) == tuple):
    if (x[0]):
        print(x[0])
        print(*x[1])
    else:
        print(x[0])
else:
    print(x)