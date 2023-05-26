W, H, X, Y, P = map(int, input().split())
cnt = 0
for i in range(P):
    playerX, playerY = map(int, input().split())
    r = H//2
    d1 = ((playerX-X)**2 + (playerY-(Y+r))**2) ** 0.5
    d2 = ((playerX-(X+W))**2 + (playerY-(Y+r))**2) ** 0.5

    if X <= playerX <= X+W and Y <= playerY <= Y+H:
        cnt += 1
    elif d1 <= r:
        cnt += 1
    elif d2 <= r:
        cnt += 1
print(cnt)