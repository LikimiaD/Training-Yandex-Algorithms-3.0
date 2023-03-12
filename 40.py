from collections import deque

file = open("input.txt", "r")

N = int(file.readline().rstrip())

DICT = {key : [] for key in range(1,N+1)}

M = int(file.readline().rstrip())

for _ in range(M):
    text = list(file.readline().rsplit())
    for num in text[1:]:
        DICT[num] = text[0]


start, end = map(int, file.readline().rstrip().split(' '))

visited = {key:False for key in DICT.keys()}

def bfs(graph, visited, start, end):
    queue = deque([(start, 0)])
    visited[start] = True
    while queue:
        node, steps = queue.popleft()
        if node == end:
            return steps
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, steps + 1))
    return -1

print(bfs(DICT, visited, start, end))