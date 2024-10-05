from collections import deque

N = int(input())
sequence = list(map(int, input().split()))
sequence.sort()

negative = deque()
zero = deque()
positive = deque()

i = 0
while i < N and sequence[i] < 0:
    if len(negative) < 2 or negative[0] > negative[-1]:
        negative.append(sequence[i])
    else:
        negative.appendleft(sequence[i])
    i += 1

while i < N and sequence[i] == 0:
    zero.append(0)
    i += 1

j = N - 1
while j >= i:
    if len(positive) < 2 or positive[0] < positive[-1]:
        positive.append(sequence[j])
    else:
        positive.appendleft(sequence[j])
    j -= 1

answer = []

if len(negative) < 2 or negative[0] < negative[-1]:
    answer += negative
else:
    answer += reversed(negative)

answer += zero

if len(positive) < 2 or positive[0] < positive[-1]:
    answer += positive
else:
    answer += reversed(positive)

print(*answer)
