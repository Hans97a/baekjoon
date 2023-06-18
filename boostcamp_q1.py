arr = sorted(list(map(int, input().split())))
result = []
check = []
for num in arr:
    cnt = arr.count(num)
    if cnt >= 2:
        if num not in check:
            result.append(cnt)
            check.append(num)


print(result)
