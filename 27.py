file = open('input.txt', 'r') 
mainN, secondN = map(int, file.readline().split()) 
LIST = [[float('-Inf')] + list(map(int, file.readline().rstrip('\n').split(' '))) if _ != 0 else [float('-Inf')] * (secondN + 1) for _ in range(0, mainN+ 1)] 
file.close() 
 
MOVES = [[[] for _ in range(0,secondN+1)] for _ in range(0, mainN+1)]
 
for i in range(1,mainN+1): 
    for j in range(1, secondN + 1): 
        if i == 1 and j == 1: 
            pass 
        else:
            value1 = LIST[i-1][j]
            value2 = LIST[i][j-1]
            if max(value1,value2) == value1:
                MOVES[i][j] = MOVES[i-1][j] + ['D']
            else:
                MOVES[i][j] = MOVES[i][j-1] + ['R']

            LIST[i][j] = max(LIST[i-1][j], LIST[i][j-1]) + LIST[i][j] 

print(LIST[-1][-1])
print(*MOVES[-1][-1])