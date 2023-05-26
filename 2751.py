import sys
N=int(input())
a=[]
for i in range(N):
    a.append(int(sys.stdin.readline().rstrip()))
a.sort()
print(*a, sep='\n')