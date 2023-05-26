# 정석이지만 메모리 초과
N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))
cntArr = [arr.count(i) for i in range(len(arr)+1)]
for i in range(len(cntArr)):
    if i == 0:
        continue
    else:
        cntArr[i] += cntArr[i-1]
output = [0] * (len(arr)+1)
for i in range(len(arr)-1, 0-1, -1):
    ck = arr[i]
    output[cntArr[ck]]= arr[i]
    cntArr[ck] -= 1
output.pop(0)
for i in output:
    print(i)


# 내장함수 사용

N = int(input())
arr=[]
for i in range(N):
    arr.append(int(input()))
arr.sort()
print(arr)


import sys
N= int(input())
arr=[0]*10001

for i in range(N):
    arr[int(sys.stdin.readline().rstrip())] += 1

for i in range(len(arr)):
    for j in range(arr[i]):
        print(i)