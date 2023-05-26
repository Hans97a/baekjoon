N=int(input())
if N==1: 0
else:
    arr=[]
    temp=N
    for i in range(2, N+1, 1):
        if temp==0: break
        if temp%i==0:
            while temp%i == 0:
                arr.append(i)
                temp= temp//i
    for i in arr:
        print(i)