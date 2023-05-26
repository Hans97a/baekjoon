N=int(input())
people=[ input().split() for i in range(N)]
result=[ 0 for i in range(N)]
for i in range(len(people)):
    for j in range(len(people)):
        if int(people[i][0])<int(people[j][0]) and int(people[i][1])<int(people[j][1]):
            result[i]+=1

for i in result:
    print(i+1, end=' ')
