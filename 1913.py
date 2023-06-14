n = int(input())
num = int(input())

result = []
arr = [[0] * n for i in range(n)]


di = [1, 0, -1, 0]  # 하 우 상 좌
dj = [0, 1, 0, -1]

number = n * n
i = -1
j = 0

start = n
i_check = j_check = 1
direction = -1
first = True
cnt = 0
while number != 0:
    direction = (direction + 1) % 4

    for k in range(start):
        i, j = i + di[direction], j + dj[direction]
        arr[i][j] = number
        number -= 1

    if first:
        start -= 1
        first = False
    else:
        cnt += 1
        if cnt == 2:
            start -= 1
            cnt = 0

result = []
for i, line in enumerate(arr):
    print(*line, sep=" ")
    if num in line:
        for j in range(len(line)):
            if arr[i][j] == num:
                result.append([i + 1, j + 1])
                break
print(*result[0], sep=" ")
