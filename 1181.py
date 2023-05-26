import sys
N = int(input())
arr = []
for i in range(N):
    arr.append(sys.stdin.readline().rstrip())

arr = set(arr)
arr = sorted(arr, key=lambda x: (len(x), x))
print(*arr, sep='\n')