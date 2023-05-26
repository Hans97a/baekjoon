N=int(input())
M=1
result=[]
for i in range(N-M):
    temp=0
    for j in range(len(str(M))):
        temp+=int(str(M)[j])
    temp+=M
    if temp==N:
        result.append(M)
    else:
        M+=1
if result:
    print(min(result))
else:
    print(0)