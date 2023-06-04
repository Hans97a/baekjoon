import sys


while True:
    user = sys.stdin.readline()
    if user[0] == ".":
        break

    stack = []

    for char in user:
        if char in ["(", "["]:
            stack.append(char)
        elif char in [")", "]"]:
            if stack:
                comp = stack.pop()
                if char == ")" and comp == "(":
                    continue
                elif char == "]" and comp == "[":
                    continue
                else:
                    stack.append("(")
                    break
            else:
                stack.append("(")
                break
    print("no" if stack else "yes")
