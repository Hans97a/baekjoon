# 시간 초과
# T = int(input())
# for i in range(T):
#     n = int(input())
#     a = 0
#     b = 10000
#     arr = [False, False] + [True]*(n-1)
#     primes = []
#     for j in range(2, n+1, 1):
#         if arr[j]:
#             for k in range(2*j, n+1, j):
#                 arr[k] = False
#             primes.append(j)
#     for j in range(len(primes)):
#         if 2*primes[j] == n:
#             a = b = primes[j]
#             break
#         else:
#             for k in range(j+1, len(primes)):
#                 if b-a > primes[k]-primes[j] and primes[k]+primes[j] == n:
#                     a = primes[j]
#                     b = primes[k]
#     if a != 0 and b != 10000:
#         print(a, b)

def func(a):
    cnt=0
    for i in range(2, int(a**0.5)+1):
        if a%i==0:
            cnt+=1
            break
    return cnt
T=int(input())

for i in range(T):
    a=int(input())
    compA=a//2
    compB=a//2
    while True:
        if func(compA)==0:
            if func(compB)==0:
                print(compA, compB)
                break
        compA-=1
        compB+=1