arr = [[0] * 100 for i in range(100)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = 1
result = 0

for line in arr:
    result += sum(line)
print(result)
