a=input()
A=[]
for i in range(len(a)):
    for j in range(len(a)+1):
        if a[i:j] != '':
            A.append(a[i:j])
A=set(A)
print(len(A))