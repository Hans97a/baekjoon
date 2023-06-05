N, M = map(int, input().split())
result = []


def dfs(idx):
    global N, M, result

    if len(result) == M:
        print(*result, sep=" ")
        return

    for i in range(idx, N + 1):
        result.append(i)
        dfs(i)
        result.pop()


dfs(1)
