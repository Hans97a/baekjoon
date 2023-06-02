import sys

N, K = map(int, input().split())

arr = [float(sys.stdin.readline()) for _ in range(N)]


jul = [num for num in arr]
bo = [num for num in arr]
jul.sort()
bo.sort()


if not K == 0:
    for i in range(K):
        bo[i], bo[-i - 1] = bo[K], bo[-K - 1]

    jul = jul[K:-K]

    print("%.2f" % (sum(jul) / len(jul) + 0.00000001))
    print("%.2f" % (sum(bo) / len(bo) + 0.00000001))
else:
    print("{:.2f}".format(sum(jul) / len(jul)))
    print("{:.2f}".format(sum(bo) / len(bo)))
