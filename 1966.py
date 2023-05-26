n = int(input())
result = []
for i in range(n):
    queue = []
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    for j in range(N):
        queue.append([arr[j], j])
    cnt = 0
    while queue:
        max_p = max([el[0] for el in queue])
        priority, order = queue.pop(0)

        if max_p == priority:
            cnt += 1
            if M == order:
                result.append(cnt)
                break
        else:
            queue.append([priority, order])
print(*result, sep="\n")
