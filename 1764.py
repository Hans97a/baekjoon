import sys
from collections import Counter

N, M = map(int, input().split())
D=[]
for i in range(N+M):
    D.append(sys.stdin.readline().rstrip())
D=Counter(D)
result=[]
for key, value in D.items():
    if value==2:
        result.append(key)
result=sorted(result, key= lambda x: x)
print(len(result))
print(*result, sep='\n')

