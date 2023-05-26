a=int(input())
while a!=0:
    if a<4:
        print(1)
    else:
        b=a*2
        arr=[]
        checklist=[False, False] + [True]*(b-1)
        for i in range(2, b+1):
            if checklist[i]:
                for j in range(2*i, b+1, i):
                    checklist[j]=False
                if i>a:
                    arr.append(i)
        print(len(arr))
    a=int(input())
