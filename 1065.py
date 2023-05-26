#my Answer
def han(n):
    result=99
    if n<100:
        return n
    else:
        for i in range(100, n+1):
            a=i//100
            b=(i%100)//10
            c=i%10
            if b*2 == a+c:
                result+=1
        return result

print(han(int(input())))

#other
N=int(input())
han = 99

if N < 100:
    han = N
else:
    for i in range(100, N+1):
        a=list(map(int,str(i)))
        if a[0]-a[1] == a[1]-a[2]:
            han+=1
            
print(han)
