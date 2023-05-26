a = [int(input()) % 42 for i in range(10)]
b = []
for i in range(len(a)):
    if a[i] not in b:
        b.append(a[i])
print(len(b))