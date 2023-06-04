# DFS -> 시간 초과

# num = input()
# length = len(num)
# used = [False] * length
# result = []
# nums = []


# def dfs():
#     global num, nums, length, used

#     if len(nums) == length:
#         number = int("".join(nums))
#         if number % 30 == 0 and number not in result:
#             result.append(number)
#         return

#     for idx in range(length):
#         if not used[idx]:
#             nums.append(num[idx])
#             used[idx] = True
#             dfs()
#             nums.pop()
#             used[idx] = False


# dfs()
# print(max(result) if len(result) != 0 else -1)


num = list(input())
num.sort(reverse=True)
res = "".join(num)

if "0" in num:
    if int(res) % 30 == 0:
        print(res)
    else:
        print(-1)
else:
    print(-1)
