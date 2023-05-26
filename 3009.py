from collections import Counter
a = [list(map(int, input().split())) for i in range(3)]
x = [a[i][0] for i in range(3)]
y = [a[j][1] for j in range(3)]
x=Counter(x)
y=Counter(y)

for key, value in x.items():
    if value==1:
        print(key, end=' ')
for key, value in y.items():
    if value==1:
        print(key, end=' ')