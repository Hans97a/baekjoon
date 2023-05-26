results=[]
while True:
    a= list(map(int, input().split()))
    a.sort()
    
    if a[0]==0 and a[1]==0 and a[2]==0:
        break
    if a[0]**2 + a[1]**2 == a[2]**2:
        results.append('right')
    else:
        results.append('wrong')
print(*results, sep='\n')