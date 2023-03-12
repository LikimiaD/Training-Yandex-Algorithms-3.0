file = open('input.txt', 'r')

def show_table():
    for x in range(N):
        for y in range(N):
            print(DICT[x][y], end="\t")
        print()
N, M, S, T, Q = list(map(int, file.readline().rsplit()))

DICT = [[(0,0) for _ in range(N)] for _ in range(N)]


for _ in range(Q):
    x,y = list(map(int, file.readline().rsplit()))
    DICT[x-1][y-1] = (0,-1)

DICT[S-1][T-1] = 0


show_table()
