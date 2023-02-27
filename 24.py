"""DICT = {
    '1' : [5, 10, 15],
    '2' : [2, 10, 15],
    '3' : [5, 5, 5],
    '4' : [20, 20, 1],
    '5' : [20, 1, 1],
}
DICT['1'].append(DICT['1'][0])
DICT['2'].append(min(DICT['1'][0]+DICT['2'][0], DICT['2'][1]))
DICT['3'].append(min(DICT['1'][0]+DICT['2'][0]+DICT['3'][0],
                     DICT['1'][1]+DICT['3'][0],
                     DICT['1'][0]+DICT['2'][1],
                     DICT['1'][2]))
for i in range(4, len(DICT)+1):
    DICT[str(i)].append(min(DICT[str(i-1)][3]+DICT[str(i)][0],
                       DICT[str(i-2)][3]+DICT[str(i-1)][1],
                       DICT[str(i-3)][3]+DICT[str(i-2)][2]))

for key,value in DICT.items():
    print(key,value)"""

f = open('input.txt', 'r')
N = int(f.readline())
DICT = {str(i): list(int(x) for x in f.readline().rstrip('\n').split(' ') if x) for i in range(1, N+1)}
f.close()
for i in range(0, -3, -1):
    DICT[str(i)] = [float('inf'),float('inf'),float('inf'),0]

for i in range(1, N+1):
    if (i == 1):
        DICT[str(i)].append(DICT['1'][0])
    else:
        DICT[str(i)].append(min(DICT[str(i-1)][3]+DICT[str(i)][0],
                        (DICT[str(i-2)][3]+DICT[str(i-1)][1]),
                        (DICT[str(i-3)][3]+DICT[str(i-2)][2])))
for i in range(0, -3, -1):
    DICT.pop(str(i))
print(list(DICT.values())[-1][3])