k = int(input())
s = input().split()[0]

unique = set(s)
list_numbers = []
for w in unique:
    head, end, counter = 0, 0, 0
    char_count = 0
    while end < len(s):
        if s[end] == w:
            char_count += 1
        end += 1
        counter = end - head - char_count
        if counter > k:
            if s[head] == w:
                char_count -= 1
            head += 1
        else:
            list_numbers.append(end - head)

print(max(list_numbers))