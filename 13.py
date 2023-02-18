f = open('input.txt', 'r')
text = f.read().rstrip('\n')
f.close()
STACK = []
x = y = 0
for symbol in text:
    if symbol.isdigit():
        STACK.append(int(symbol))
    else:
        match symbol:
            case "*":
                x = STACK[-1]
                y = STACK[-2]
                STACK.pop()
                STACK.pop()
                STACK.append(x*y)
            case "/":
                x = STACK[-1]
                y = STACK[-2]
                STACK.pop()
                STACK.pop()
                STACK.append(int(x/y))
            case "-":
                x = STACK[-1]
                y = STACK[-2]
                STACK.pop()
                STACK.pop()
                STACK.append(y-x)
            case "+":
                x = STACK[-1]
                y = STACK[-2]
                STACK.pop()
                STACK.pop()
                STACK.append(x+y)

w = open('output.txt', 'w')
w.write(str(STACK[0]))
w.close()