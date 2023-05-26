num= input("")
A=""
B=""

for i in range(len(num)):
    if num[i] ==' ':
        B=num[i+1:len(num)+1]
        break
    else:
        A+=num[i]

A=int(A)
B=int(B)

if(A > B):
    print(">")
elif(A < B):
    print("<")
else:
    print("==")