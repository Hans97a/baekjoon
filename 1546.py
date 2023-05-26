N = int(input())
score = input().split()
score = list(map(int, score))
M = max(score)

for i in range(len(score)):
    score[i] = (score[i]/M)*100
print(sum(score)/N)