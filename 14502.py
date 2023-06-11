import copy

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]
di = [1, 0, 0, -1]
dj = [0, 1, -1, 0]
max_result = 0


def bfs():
    global max_result, di, dj
    copy_arr = copy.deepcopy(arr)
    result = 0
    temp = []
    for i in range(N):
        for j in range(M):
            if copy_arr[i][j] == 2:
                temp.append([i, j])
    while temp:
        a, b = temp.pop(0)
        for i in range(4):
            ni = a + di[i]
            nj = b + dj[i]

            if 0 <= ni < N and 0 <= nj < M:
                if copy_arr[ni][nj] == 0:
                    copy_arr[ni][nj] = 2
                    temp.append([ni, nj])
    for i in copy_arr:
        for j in i:
            if j == 0:
                result += 1
    max_result = max(result, max_result)


def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(cnt + 1)
                arr[i][j] = 0


wall(0)
print(max_result)
