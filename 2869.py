import math
A, B, V=map(int, input().split())
print(math.ceil((V-A)/(A-B))+1)
# day=1
# leng=0
# while True:
#     leng=leng+A
#     if V<=leng:
#         break
#     leng=leng-B
#     day+=1
# print(day)