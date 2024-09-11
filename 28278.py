import sys

input = sys.stdin.readline

stack = []

N = int(input())

for _ in range(N):
    input_data = input()

    if input_data[0] == "1":
        stack.append(input_data.split()[1])
    else:
        num = int(input_data)

        if num == 2:
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif num == 3:
            print(len(stack))
        elif num == 4:
            print(0 if stack else 1)
        else:
            print(stack[-1] if stack else -1)
