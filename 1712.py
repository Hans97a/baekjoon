A, B, C = map(int, input().split())

if B >= C:
    print(-1)
else:
    temp1 = C-B
    temp2 = A//temp1 + 1
    print(temp2)