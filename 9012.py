T = int(input())

for i in range(T):
    stack = []
    string = input()
    check = False
    for char in string:
        if char == "(":
            stack.append(char)
        else:
            if stack:
                stack.pop()
            else:
                check = True
                break
    print("NO" if stack or check else "YES")
