N=int(input())
A=input().split()
max=-1000000
min=1000000
for i in range(N):
    if int(A[i])>max:
        max=int(A[i])
    if int(A[i])<min:
        min=int(A[i])
print(min, max)