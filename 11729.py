N = int(input())
cnt = 0
a = 1
b = 2
c = 3
arr=[]

def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n-1, a, c, b)
        move(n, a, c)
        hanoi(n-1, b, a, c)

def move(n, a, c):
    global cnt
    cnt += 1
    global arr
    arr.append([a, c])
hanoi(N, a, b, c)
print(cnt)
for i in arr:
    print(i[0], i[1])