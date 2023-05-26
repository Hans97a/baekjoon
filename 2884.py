M = ""
H = ""

while True:
    a = input()
    for i in range(len(a)):
        if a[i] == ' ':
            M = a[i+1:len(a)+1]
            break
        else:
            H += a[i]
    H = int(H)
    M = int(M)
    if((0 <= H <= 23) and (0 <= M <= 59)):
        break


if(M >= 45):
    print(H, M-45)
else:
    if(H == 0):
        H = 23
        print(H, (M+60)-45)
    else:
        print(H-1, (M+60)-45)