N, M= map(int, input().split())
s=set()
for i in range(N):
    temp= input().rstrip()
    s.add(temp)
cnt=0
for i in range(M):
    temp=input()
    if temp in s:
        cnt+=1
print(cnt)
