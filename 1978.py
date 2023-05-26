N=int(input())
a=map(int, input().split())
result=0
for i in a:
    count=0
    for j in range(1, i+1, 1):
        if i%j==0:
            count+=1
    if count==2:
        result+=1
print(result)