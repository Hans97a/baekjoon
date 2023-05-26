def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        a=0
        b=1
        cnt=a+b
        for i in range(n-2):
            a=b
            b=cnt
            cnt=a+b
        return cnt

n=int(input())
print(fibo(n))