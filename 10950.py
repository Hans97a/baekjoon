# a=int(input())

# for i in range(a):
#     inputA=""
#     inputB=""
#     while True:
#         temp=input()
#         for j in range(len(temp)):
#             if(temp[j]==' '):
#                 inputB=temp[j+1]
#                 break
#             else:
#                 inputA+=temp[j]
#         inputA=int(inputA)
#         inputB=int(inputB)
#         if((inputA>0) and (inputB<10)):
#             break
#     print(inputA+inputB)

a=input()

A, B= a.split()
print(A+B)
print(type(A))