from functools import lru_cache
M=int(input())
N=int(input())
so=[]
@lru_cache
def func():
    for i in range(M, N+1, 1):
        count=0
        for j in range(1, i+1, 1):
            if i%j==0:
                count+=1
        if count==2:
            so.append(i)
    if sum(so)==0:
        print(-1)
    else:
        print(sum(so))
        print(min(so))
func()