from collections import defaultdict, deque


def solution(n, roads, sources, destination):
    # 부대위치를 기준으로 모든 지점의 거리 (일차원 테이블)
    des = [-1 for _ in range(n + 1)]
    des[destination] = 0
    # roads를 바탕으로 구성한 길 정보
    graph = defaultdict(list)
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    # bfs를 통한 모든 지점 최단 경로
    Q = deque([destination])
    visited = set([destination])
    while Q:
        node = Q.popleft()
        for x in graph[node]:
            if x not in visited:
                visited.add(x)
                des[x] = des[node] + 1
                Q.append(x)

    return list(des[s] for s in sources)


print(solution(3, [[1, 2], [2, 3]], [2, 3], 1))
