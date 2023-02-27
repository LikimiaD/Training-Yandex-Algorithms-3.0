N = int(10)
LIST = sorted(list(map(int, "682 2517 2478 2816 4980 5839 6414 7667 8802 8995".split())))

TRASH = [0] * N

TRASH[1] = LIST[1] - LIST[0]
if N > 2:
    TRASH[2] = LIST[2] - LIST[0]
    for i in range(3,N):
        TRASH[i] = min(TRASH[i-2],TRASH[i-1]) + LIST[i] - LIST[i - 1]
print(TRASH[-1])