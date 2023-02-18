n = int(input())
carriages = list(map(int, input().split()))

next_carriage_to_place = 1  # следующий вагон, который нужно поместить на своё место
stack = []  # стек вагонов в тупике

for carriage in carriages:
    if carriage == next_carriage_to_place:
        next_carriage_to_place += 1  # переходим к следующему вагону, который нужно поместить на своё место
    else:
        # ищем самый левый вагон на пути 1, который находится не на своём месте и правее текущего вагона
        while stack and stack[-1] == next_carriage_to_place:
            stack.pop()
            next_carriage_to_place += 1
        if carriage == next_carriage_to_place:
            next_carriage_to_place += 1  # переходим к следующему вагону, который нужно поместить на своё место
        else:
            stack.append(carriage)  # помещаем вагон в тупик

# проверяем, что все вагоны были помещены на свои места
while stack and stack[-1] == next_carriage_to_place:
    stack.pop()
    next_carriage_to_place += 1

if not stack:
    print("YES")
else:
    print("NO")