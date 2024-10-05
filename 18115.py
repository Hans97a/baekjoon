from collections import deque

N = int(input())
skills = list(map(int, input().split()))
sequence = deque()

skills.reverse()

for i in range(N):
    if skills[i] == 1:
        sequence.appendleft(i + 1)
    elif skills[i] == 2:
        sequence.insert(1, i + 1)
    else:
        sequence.append(i + 1)

print(*sequence)
