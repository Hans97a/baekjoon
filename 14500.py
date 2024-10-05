answer = 0
dy, dx = [1, -1, 0, 0], [0, 0, -1, 1]

N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]


def dfs(arr, cnt):
    global answer

    if len(arr) == 4:
        if cnt > answer:
            answer = cnt

        return

    for y, x in arr:
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] is False:
                arr.append((ny, nx))
                visited[ny][nx] = True
                dfs(arr, cnt + paper[ny][nx])
                visited[ny][nx] = False
                arr.pop()


for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs([(i, j)], paper[i][j])


print(answer)
