n = int(input())
trains = list(map(int, input().split()))

_next = 1
STACK = []

for train in trains:
    if train == _next:
        _next += 1 
    else:
        while STACK and STACK[-1] == _next:
            STACK.pop()
            _next += 1
        if train == _next:
            _next += 1
        else:
            STACK.append(train)

while STACK and STACK[-1] == _next:
    STACK.pop()
    _next += 1

print("YES" if not STACK else "NO")