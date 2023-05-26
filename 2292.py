N=int(input())
if N==1:
    cnt=1
    print(cnt)
else:
    a=6+1
    cnt=2
    while a<N:
        a+=6*cnt
        cnt+=1
    print(cnt)