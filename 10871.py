N, X=map(int, input().split())
A=input().split()

for i in range(N):
    if int(A[i]) < X:
        print(int(A[i]), end=' ')