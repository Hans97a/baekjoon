T=int(input())

for t in range(T):
    H, W, N= map(int, input().split())
    Y=1
    X=1
    
    if H==1:
        for i in range(N-1):
            X+=1
    else:
        for i in range(N-1):
            if Y%H==0 and Y !=1:
                Y=1
                X+=1
            else:
                Y+=1
    print(Y*100+X)