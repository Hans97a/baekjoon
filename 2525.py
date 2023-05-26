H=""
M=""

while True:
    a=input()
    for i in range(len(a)):
        if a[i]==' ':
            M=a[i+1:len(a)+1]
            break
        else:
            H+=a[i]
    D=int(input())
    H=int(H)
    M=int(M)
    if ((0<=H<=23) and (0<=M<=59) and (0<=D<=1000)):
        break

tempA=D//60
tempB=D%60

if (M+tempB >=60):
    M=(M+tempB)%60
    H+=1
    if(H==24):
        H=0
else:
    M=M+tempB

for i in range(tempA):
    if H==23:
        H=0
    else:
        H+=1

print(H, M)