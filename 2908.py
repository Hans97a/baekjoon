a=input().split()
comp1 = comp2 = ''
for i in range(2,0-1, -1):
    comp1+=a[0][i]
    comp2+=a[1][i]
int(comp1); int(comp2)
if comp1>comp2:
    print(comp1)
else:
    print(comp2)