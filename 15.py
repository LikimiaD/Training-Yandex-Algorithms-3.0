n = int("10")
a = list(map(int, "1 2 3 2 1 4 2 5 3 1".split()))

min_index = [-1] * n
current_min_index = 0

for i in range(1, n):
    if a[i] < a[current_min_index]:
        current_min_index = i
    min_index[i] = current_min_index

for i in range(n):
    if min_index[i] == i:
        print("-1", end=" ")
    else:
        print(min_index[i], end=" ")