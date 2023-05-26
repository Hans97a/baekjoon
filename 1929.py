M, N=map(int, input().split())
a=[False, False] + [True] * (N-1)
num=[]
for i in range(2, N+1):
    if a[i]:
        for j in range(2*i, N+1, i):
            a[j]=False
        if i>=M:
            num.append(i)
for i in num:
    print(i)