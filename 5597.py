a=[ int(input()) for i in range(28)]
ans = []

for i in range(1, 31):
    if a.count(i)== 0:
        ans.append(i)
ans.sort()
for i in ans:
    print(i)