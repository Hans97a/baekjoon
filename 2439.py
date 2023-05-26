a = int(input())
temp = a-1

for i in range(a):
    if temp != -1:
        print(' '*temp, end='')
        temp -= 1
    print('*'*(i+1))