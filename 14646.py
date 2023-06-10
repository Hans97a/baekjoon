N = int(input())

arr = list(map(int, input().split()))
visited = [False] * (len(arr) + 1)
sticker = 0
result = 0
for i in range(2 * N):
    idx = arr[i]
    if not visited[idx]:
        visited[idx] = True
        sticker += 1
    else:
        sticker -= 1
    result = max(result, sticker)
print(result)
