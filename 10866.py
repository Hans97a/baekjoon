from collections import deque
import sys


class CustomDeque(deque):
    def push_front(self, num):
        dq.appendleft(int(num))

    def push_back(self, num):
        dq.append(int(num))

    def pop_front(self):
        print(dq.popleft() if len(dq) != 0 else -1)

    def pop_back(self):
        print(dq.pop() if len(dq) != 0 else -1)

    def size(self):
        print(len(dq))

    def empty(self):
        print(1 if len(dq) == 0 else 0)

    def front(self):
        print(dq[0] if len(dq) != 0 else -1)

    def back(self):
        print(dq[-1] if len(dq) != 0 else -1)


dq = CustomDeque()

for i in range(int(input())):
    command = sys.stdin.readline().split()
    if len(command) == 2:
        eval("dq." + command[0] + f"({command[1]})")
    else:
        eval("dq." + command[0] + "()")
