CLOSE = [']', '}', ')']

CHECKER = {
    ']' : '[',
    '}' : '{',
    ')' : '(',
}

Stack = []
f = open('input.txt', 'r')
text = f.read().rstrip('\n')
f.close()

for symbol in text:
    if not symbol in CLOSE:
        Stack.append(symbol)
    else:
        if len(Stack) > 0 and Stack[-1] == CHECKER[symbol]:
            Stack.pop()
        else:
            Stack.append(symbol)
w = open('output.txt', 'w')
w.write('yes' if len(Stack) == 0 else 'no')
w.close()