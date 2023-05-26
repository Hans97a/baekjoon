N=int(input())
arr = list(map(int, input().split()))

temp = sorted(list(set(arr)))
dic= { temp[i]: i for i in range(len(temp))}
for i in range(len(arr)):
    print(dic[arr[i]], end=' ')