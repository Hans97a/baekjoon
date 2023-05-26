arr = list(map(int, input().split(" ")))

arr.remove(max(arr))
arr.remove(min(arr))
print(arr[0])
