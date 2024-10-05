from collections import deque
import sys

input = sys.stdin.readline
dq = deque()
arr = []


for i in range(int(input())):
    operation = input().strip()
    if len(operation) == 1:
        operation = int(operation)

        if operation == 3:
            if dq:
                print(dq.popleft())
            else:
                print(-1)
        elif operation == 4:
            if dq:
                print(dq.pop())
            else:
                print(-1)
        elif operation == 5:
            print(len(dq))
        elif operation == 6:
            print(0 if dq else 1)
        elif operation == 7:
            print(dq[0] if dq else -1)
        else:
            print(dq[-1] if dq else -1)

    else:
        operation, num = map(int, operation.split())

        if operation == 1:
            dq.appendleft(num)
        else:
            dq.append(num)
