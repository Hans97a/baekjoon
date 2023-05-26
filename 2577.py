a = []
for i in range(3):
    a.append(int(input()))
abc=a[0]*a[1]*a[2]
for i in range(10):
    count=0
    for j in range(len(str(abc))):
        if str(i)==str(abc)[j]:
            count+=1
    print(count)