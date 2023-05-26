num=666
N=int(input())
check=0

while True:
    if '666' in str(num):
        check+=1
    if check==N:
        break
    num+=1
print(num)