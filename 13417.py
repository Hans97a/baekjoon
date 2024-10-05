from collections import deque

T = int(input())

for _ in range(T):
    N = int(input())
    alphabets = input().split()

    Q = deque()

    Q.append(alphabets.pop(0))

    for alphabet in alphabets:
        if Q[0] >= alphabet:
            Q.appendleft(alphabet)
        else:
            Q.append(alphabet)

    print("".join(Q))
