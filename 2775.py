T=int(input())
for t in range(T):
    k=int(input())
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(i+1)
    for i in range(k):
        temp=arr.copy()
        for j in range(n):
            if j==0:
                arr[j]=temp[j]
            elif j+1<n:
                arr[j]= sum(temp[:j+1])
            else:
                arr[j]= sum(temp)
    print(arr[n-1])