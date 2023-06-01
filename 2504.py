string = input()

stack = []
result = 0
check = False
for gwalho in string:
    if check:
        print(0)
        break

    if gwalho == ")":
        if len(stack) != 0:
            compare = stack.pop()
            if compare == "(":
                result += 2
            else:
                check = True
        else:
            check = True
    elif gwalho == "]":
        if len(stack) != 0:
            compare = stack.pop()
            if compare == "[":
                result += 2
            else:
                check = True
        else:
            check = True
    else:
        stack.append(stack)
