i = 1
while True:
    line = input()
    if "-" in line:
        break

    stack = []
    cnt = 0
    for idx, char in enumerate(line):
        if char == "{":
            if not idx == len(line) - 1:
                stack.append(char)
            else:
                cnt += 1
        else:
            if not stack:
                stack.append("{")
                cnt += 1
            else:
                stack.pop()

    if stack:
        cnt += len(stack) // 2

    print(f"{i}. {cnt}")
    i += 1
