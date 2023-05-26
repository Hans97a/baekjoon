n, m = map(int, input().split())
a= []
b= []
for i in range(n*2):
    if i < n:
        b.append(list(map(int, input().split())))
    else:
        a.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        print(a[i][j] + b[i][j], end=' ')
    print()