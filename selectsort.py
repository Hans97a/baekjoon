a = [5, 4, 3, 6, 1, 2, 7, 9, 11, 10, 13]

point = 0
num = 1000
for i in range(len(a)):
    for j in range(point, len(a)):
        if num > a[j]:
            num = a[j]
            point = j

    if i != point:
        a[i], a[point] = a[point], a[i]
    num = 1000
    point = i + 1


print(a)
