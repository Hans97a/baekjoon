def selfNum():
    result=[]
    for i in range(1, 10000+1):
        temp=i
        a = temp//1000; temp%=1000
        b = temp//100; temp%=100
        c = temp//10; temp%=10
        d = temp
        result.append(i+a+b+c+d)
    for i in range(1, 10000+1):
        if i not in result:
            print(i)
selfNum()

# for i in sorted(set(range(10001))-set([n+sum(map(int,str(n))) for n in range(10000)])):print(i)