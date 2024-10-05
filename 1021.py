from collections import deque


N, M = map(int, input().split())
sequnce = list(map(int, input().split()))
Q = deque([i + 1 for i in range(N)])

cnt = 0
result = 0

while cnt != M:
    if Q[0] == sequnce[0]:
        Q.popleft()
        sequnce.pop(0)
        cnt += 1
    else:
        position = Q.index(sequnce[0])

        if len(Q) // 2 >= position:
            Q.rotate(-1)
        else:
            Q.rotate(1)

        result += 1

print(result)
