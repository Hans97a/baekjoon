stack = []

n = int(input())

arr = [input() for i in range(n)]


for element in arr:
    element = element.split(" ")

    if len(element) == 2:
        stack.append(int(element[1]))
    elif element[0] == "pop":
        if len(stack) > 0:
            print(stack.pop(len(stack) - 1))
        else:
            print(-1)
    elif element[0] == "size":
        print(len(stack))
    elif element[0] == "empty":
        print(1 if len(stack) == 0 else 0)
    else:
        print(stack[len(stack) - 1] if len(stack) > 0 else -1)
