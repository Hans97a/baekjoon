N1, N2 = map(int, input().split())
group1 = list(input())
group2 = list(input())
second = int(input())


group1.reverse()
totalAnt = group1 + group2

for _ in range(second):
    for i in range(len(totalAnt) - 1):
        if totalAnt[i] in group1 and totalAnt[i + 1] in group2:
            totalAnt[i], totalAnt[i + 1] = totalAnt[i + 1], totalAnt[i]

            if totalAnt[i + 1] == group1[-1]:
                break

print("".join(totalAnt))
