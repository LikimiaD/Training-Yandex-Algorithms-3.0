STACK = []
ENDLINE = "\n"
exitText = ""
f = open('input.txt', 'r')
w = open('output.txt', 'w')
while exitText != "bye":
    text = f.readline().rstrip('\n').split(' ')
    match text[0]:
        case "push":
            w.write("ok" + ENDLINE)
            STACK.append(str(text[1]))
        case "front":
            if (len(STACK)):
                w.write(STACK[0] + ENDLINE)
            else:
                w.write("error" + ENDLINE)
        case "size":
            w.write(str(len(STACK)) + ENDLINE)
        case "clear":
            w.write("ok" + ENDLINE)
            STACK = []
        case "pop":
            if (len(STACK)):
                w.write(STACK[0] + ENDLINE)
                STACK.remove(STACK[0])
            else:
                w.write("error" + ENDLINE)
        case "exit":
            w.write("bye" + ENDLINE)
            exitText = "bye"
f.close()
w.close()