import sys
input = sys.stdin.readline


def GCD(A, B):
    if B == 0:
        return A
    return GCD(B, A % B)


N = int(input())
arr = []

for i in range(N):
    arr.append(int(input()))
arr.sort(key=lambda x: -x)
temp = []
for i in range(N-1):
    temp.append(arr[i]-arr[i+1])
temp.sort(key=lambda x: -x)

gcd = temp[0]
for i in range(1, N-1):
    gcd = GCD(gcd, temp[i])

result = set()
for i in range(int(gcd**0.5)):
    i += 1
    if gcd % i == 0:
        result.add(i)
        result.add(gcd//i)
result.remove(1)
result=list(result)
result.sort()

print(*result, end=' ')