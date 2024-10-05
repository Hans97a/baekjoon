# from collections import deque

# N = int(input())  # 장애물 수

# start_i, goal_j = map(int, input().split())

# barriers = [list(map(int, input().split())) for _ in range(N)]
# barriers.sort(key=lambda x: x[0])
# result_dict = dict()

# Q = deque([(start_i, 0, 0, 0)])


# def can_go(order, now_i):
#     result = 0
#     for i in range(order, N):
#         if barriers[i][1] <= now_i <= barriers[i][2]:
#             result += 1
#             break
#     return result == 0


# while Q:
#     i, j, order, cnt = Q.popleft()

#     if can_go(order, i):
#         cnt += goal_j - j

#         if cnt in result_dict:
#             result_dict[cnt].append(i)
#         else:
#             result_dict[cnt] = [i]

#     for k in range(order, N):
#         barrier = barriers[k]

#         if barrier[0] > j and barrier[1] <= i <= barrier[2]:
#             Q.append(
#                 (
#                     barrier[1],
#                     barrier[0],
#                     k + 1,
#                     cnt + abs(barrier[1] - i) + abs(barrier[0] - j),
#                 )
#             )
#             Q.append(
#                 (
#                     barrier[2],
#                     barrier[0],
#                     k + 1,
#                     cnt + abs(barrier[2] - i) + abs(barrier[0] - j),
#                 )
#             )
#             break


# r = min(result_dict.keys())

# print(r)
# results = sorted(list(set(result_dict[r])))
# print(len(results), *results)
