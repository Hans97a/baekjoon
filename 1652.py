N = int(input())

room = []
w = 0
h = 0

for i in range(N):
    str_in = input()
    room.append(str_in)

    arr = str_in.split("X")
    for el in arr:
        if len(el) >= 2:
            w += 1


for i in range(N):
    string = ""
    for j in range(N):
        string += room[j][i]
    arr = string.split("X")
    for el in arr:
        if len(el) >= 2:
            h += 1
print(w, h)
