a= []

for i in range(5):
    a.append(int(input()))
    
print(sum(a)//len(a))
a.sort()
print(a[len(a)//2])