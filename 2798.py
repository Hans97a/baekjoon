N, M = map(int, input().split())
arr = [i for i in map(int, input().split())]
gap = 999999
for i in range(len(arr)-2):
    for j in range(i+1, len(arr)-1):
        for k in range(j+1, len(arr)):
            if arr[i]+arr[j]+arr[k] <= M and M - (arr[i]+arr[j]+arr[k]) < gap:
                gap = M - (arr[i]+arr[j]+arr[k])
                save = arr[i]+arr[j]+arr[k]
print(save)