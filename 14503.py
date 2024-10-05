# N, M = map(int, input().split())

# r, c, d = map(int, input().split())

# arr = []
# answer = 1

# for _ in range(N):
#     temp = list(map(int, input().split()))
#     arr.append(temp)


# arr[r][c] = -1

# dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]


# while arr[r][c] != 1:
#     can_go = False
#     for _ in range(4):
#         d -= 1

#         if d == -1:
#             d = 3

#         nr, nc = r + dr[d], c + dc[d]

#         if arr[nr][nc] == 0:
#             r, c = nr, nc
#             arr[r][c] = -1
#             answer += 1
#             can_go = True
#             break

#     if not can_go:
#         r += dr[d - 2]
#         c += dc[d - 2]

# print(answer)


N, M = map(int, input().split())

r, c, d = map(int, input().split())

room = []
for _ in range(N):
    room.append(list(map(int, input().split())))

room[r][c] = -1
answer = 1

dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]

while room[r][c] != 1:
    can_go = False
    for _ in range(4):
        d -= 1

        if d == -1:
            d = 3
        nr, nc = r + dr[d], c + dc[d]

        if room[nr][nc] == 0:
            r, c = nr, nc
            room[r][c] = -1
            answer += 1
            can_go = True
            break

    if can_go is False:
        r, c = r + dr[d - 2], c + dc[d - 2]

print(answer)
