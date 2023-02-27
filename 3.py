def nearest(lst, target):
  return min(lst, key=lambda x: abs(x-target))

input()
LIST = list(map(int, input().split(' ')))
MAX = max(LIST)
input()
cheliks = list(map(int, input().split(' ')))
for num in cheliks:
    x = nearest(LIST, num)
    if num < min:
        print(len(LIST[:num]))
    elif num > min:
        if num > max:
            print(len(LIST))
        else:
            print(len(LIST[:x+1]))
    else:
        print(len(LIST[:x+1]))


    