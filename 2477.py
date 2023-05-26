M = int(input())
value = []
width = []
height = []

for i in range(6):
    a, b = map(int, input().split())
    value.append(b)
    if a == 1 or a == 2:
        width.append(b)
    else:
        height.append(b)

small = 1
value.insert(0, value[len(value)-1])
value.append(value[1])

max_width = max(width)
max_height = max(height)

for i in range(1, 7):
    if value[i-1] + value[i+1] == max_width or value[i-1] + value[i+1] == max_height:
        small *= value[i]
print(M*(max_width*max_height - small))