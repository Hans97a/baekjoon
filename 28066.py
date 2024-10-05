from collections import deque


N, K = map(int, input().split())

Q = deque(list(range(1, N + 1)))

while len(Q) != 1:
    Q.rotate(-1)
    for i in range(K - 1):
        Q.popleft()
        if len(Q) == 1:
            break

print(Q[0])
