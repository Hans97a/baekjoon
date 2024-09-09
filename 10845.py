import sys

input = sys.stdin.readline

num = int(input())

queue = []

for _ in range(num):
    operation = input().rstrip()

    if operation == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif operation == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
    elif operation == "size":
        print(len(queue))
    elif operation == "empty":
        print(0 if queue else 1)
    elif operation == "pop":
        if queue:
            print(queue[0])
            del queue[0]
        else:
            print(-1)
    else:
        x = int(operation.split()[1])
        queue.append(x)
