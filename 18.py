STACK = []
ENDLINE = "\n"
exitText = ""
f = open('input.txt', 'r')
w = open('output.txt', 'w')
while exitText != "bye":
    text = f.readline().rstrip('\n').split(' ')
    match text[0]:
        case "push_front":
            w.write("ok" + ENDLINE)
            STACK.insert(0, str(text[1]))
        case "push_back":
            w.write("ok" + ENDLINE)
            STACK.append(str(text[1]))
        case "front":
            if (len(STACK)):
                w.write(STACK[0] + ENDLINE)
            else:
                w.write("error" + ENDLINE)
        case "back":
            if (len(STACK)):
                w.write(STACK[-1] + ENDLINE)
            else:
                w.write("error" + ENDLINE)
        case "size":
            w.write(str(len(STACK)) + ENDLINE)
        case "clear":
            w.write("ok" + ENDLINE)
            STACK = []
        case "pop_front":
            if (len(STACK)):
                w.write(STACK[0] + ENDLINE)
                STACK.remove(STACK[0])
            else:
                w.write("error" + ENDLINE)
        case "pop_back":
            if (len(STACK)):
                w.write(STACK[-1] + ENDLINE)
                STACK.pop()
            else:
                w.write("error" + ENDLINE)
        case "exit":
            w.write("bye" + ENDLINE)
            exitText = "bye"
f.close()
w.close()