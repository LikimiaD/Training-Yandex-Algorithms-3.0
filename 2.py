p = int(input())
s = input()
max = None

for i in range(len(s) - p):
    k = p
    counter = 1
    for j in range(i + 1, len(s)):
        if s[j] == s[i]:
            counter += 1
        elif k > 0:
            counter += 1
            k -= 1
        else:
            break
    if (max == None):
        max = counter
    else:
        if (max < counter):
            max = counter
            
print(max)

"""
x = 2
y = "abcaz"
MAX = 0

for first in y:
    temp = x
    count = 0
    ptr = first
    for sym in y:
        if (ptr != sym) and (temp != 0):
            count += 1
            temp -= 1
        elif (ptr == sym):
            count += 1
        elif (ptr != sym) and (temp == 0):
            if MAX < count:
                MAX = count
            break
print(MAX)

"""