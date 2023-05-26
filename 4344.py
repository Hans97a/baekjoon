C=int(input())
for i in range(C):
    a=0
    temp= list(map(int,input().split()))
    N=temp[0]
    temp.pop(0)
    average=sum(temp)/N
    for j in range(len(temp)):
        if temp[j]>average:
            a+=1
    print('{:.3f}%'.format((a/N)*100))