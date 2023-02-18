
f = open('input.txt', 'r')
input1 = int(f.readline())
input2 = int(f.readline())
input3 = int(f.readline())
input4 = int(f.readline())
f.close()
count = 1

partas = input1 if input1 % 2 == 0 else input1 +1

_dict = {}

global_check = 1
def check(count):
    if (global_check <= input1):
        return count if count <= input2 else 1
    else:
        return 0

for value in range(1, int(partas/2)+1):
    count = check(count)
    global_check += 1
    left = count
    count += 1
    count = check(count)
    global_check += 1
    right = count
    count += 1
    _dict[value] = [left,right]

petya = _dict[input3][input4-1]

def checker(_dict, petya, start, end, input3, input4):
    vasya = False
    for value in range(start, end):
        if _dict[value][0] == petya and (value != input3):
            return [value, 0+1]
        elif _dict[value][1] == petya and (value != input3):
            return [value, 1+1]
        else:
            continue
    if not vasya:
        return -1

x = checker(_dict,petya,1, int(partas/2)+1, input3, input4)


w = open('output.txt', 'w')
if(type(x) == list):
    w.write("{0} {1}".format(x[0],x[1]))
else:
    w.write(str(x))
w.close()