N, K = map(int, input().split())

if K == 0:
    print(1)
else:
    up = 1
    for i in range(K):
        up *= (N-i)

    down = 1
    while True:
        if K == 1:
            break
        down *= K
        K -= 1

    print(up//down)
