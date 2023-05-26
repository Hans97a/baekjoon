# 시간초과
# N = int(input())
# have = list(map(int, input().split()))
# M = int(input())
# given = list(map(int, input().split()))

# for i in given:
#     if i in have:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')


N = int(input())
have = set(input().split())
M = int(input())
given = input().split()

for card in given:
    if card in have:
        print(1, end=' ')
    else:
        print(0, end=' ')