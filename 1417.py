N = int(input())
arr = [int(input()) for i in range(N)]

dasom = arr[0]
arr = arr[1:]
cnt = 0
if arr:
    max_num = max(arr)
    while max_num >= dasom:
        idx = arr.index(max_num)
        cnt += 1
        dasom += 1
        arr[idx] -= 1
        max_num = max(arr)
    print(cnt)
else:
    print(0)
