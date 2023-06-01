import sys

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


C, R = map(int, input().split())
K = int(input())
cnt = 1

if C * R < K:
    print(0)
    sys.exit(0)
x = y = k = 0


table = [[False] * C for n in range(R)]

for i in range(1, C * R + 1):
    if i == K:
        print(x + 1, y + 1)
        break
    else:
        table[y][x] = True
        x += dx[k]
        y += dy[k]
        if x < 0 or y < 0 or x >= C or y >= R or table[y][x]:
            x -= dx[k]
            y -= dy[k]
            k = (k + 1) % 4

            x += dx[k]
            y += dy[k]
