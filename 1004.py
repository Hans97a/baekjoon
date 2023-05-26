import sys

def check(ck1, ck2):
    if ck1 == ck2:
        return False
    else:
        return True


input = sys.stdin.readline
T = int(input())
for i in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    cnt = 0
    n = int(input())
    for j in range(n):
        px, py, r = map(int, input().split())
        d1 = ((x1-px)**2 + (y1-py)**2)**0.5
        d2 = ((x2-px)**2 + (y2-py)**2)**0.5
        if check(d1 > r, d2 > r):
            cnt += 1
    print(cnt)