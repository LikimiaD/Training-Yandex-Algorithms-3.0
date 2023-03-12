file = open('input.txt', 'r')

N = int(file.readline().rstrip('\n'))

text = [int(file.readline()) for _ in range(N)]
coupon_days = [x for x,y in enumerate(text) if y > 100]

LIST = [text if _ == 0 else  [0] * (N) for _ in range(len(coupon_days)+1)]

for x in range(1,len(coupon_days)+1):
    LIST[x][0] = LIST[0][0]

print("Стоковая")
for x in range(len(coupon_days)+1):
    print(f"{x} |\t", end="")
    for y in range(N):
        print(LIST[x][y], end='\t')
    print()

coupon = 1

LIST_1 = [(x,y) for x,y in enumerate(LIST[0].copy())]

print
for rng in coupon_days:
    if coupon:
        max_ = max(LIST[0][rng+1:])
        index_ = LIST[0][rng+1:].index(max_)
        print(index_, max_)
        LIST_1.remove((index_, max_))
        coupon -= 1
    else:
        coupon += 1 if max(LIST[0][rng+1:]) > 100 else 0

"""LIST_1.remove((0, 35))"""

for item in LIST_1:
    print(item, end = " ")
print()

    