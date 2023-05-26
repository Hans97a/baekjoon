n, k = map(int, input().split())
arr = [i for i in range(1, n + 1)]
i = k - 1
result = []
while arr:
    num = arr.pop(i)
    result.append(num)
    if len(arr) > 0:
        i = (i + k - 1) % len(arr)
print("<", end="")
print(*result, sep=", ", end="")
print(">")
