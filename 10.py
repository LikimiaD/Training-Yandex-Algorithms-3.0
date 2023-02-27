text = "hello"

DICT = {sym: 0 for sym in sorted(set(text))}

for i in range(len(text)):
    DICT[text[i]] += len(text[:i+1]) * len(text[i:])

for key,value in DICT.items():
    print(f"{key}: {value}")