A=int(input())
check=A
temp=A
count=1
while True:
    if A<10:
        temp= A*10
    temp= (temp//10)+temp%10
    temp=((A%10)*10)+(temp%10)
    if temp==check:
        break
    else:
        A=temp
        count+=1
print(count)