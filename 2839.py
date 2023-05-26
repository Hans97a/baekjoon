N = int(input())

result=123456789
for i in range(N//5+1):
    for j in range(N//3+1):
        if 5*i + 3*j == N and i + j < result:
            result= i + j
if result==123456789:
    result=-1
print(result)