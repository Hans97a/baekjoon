N, M= map(int, input().split())
dogam={}
for i in range(N):
    temp=input().rstrip()
    dogam[temp] = i+1
    dogam[i+1]=temp
arr=[]
for i in range(M):
    temp=input().rstrip()
    if temp.isdigit():
        arr.append(dogam[int(temp)])
    else:
        arr.append(dogam[temp])

print(*arr, sep='\n')