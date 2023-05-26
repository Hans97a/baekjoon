a=input()

A=int(a[0])
B=int(a[2])
C=int(a[4])

if(A==B==C):
    print(10000+A*1000)
elif(A==B):
    print(1000+A*100)
elif(B==C):
    print(1000+B*100)
elif(C==A):
    print(1000+C*100)
else:
    big=0
    temp=[A, B ,C]
    for i in temp:
        if(big<i):
            big=i
    print(big*100)