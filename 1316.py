# N = int(input())
# a = []
# cnt=0
# for i in range(N):
#     a.append(input())
# for i in a:
#     for n, j in enumerate(i):
#         if i.count(j)==1:
#             check=1
#             continue
#         else:
#             if i[n]!=i[n+1]:
#                 check=0
#                 break
#             else:
#                 i=list(i)
#                 i[n]='0'
#                 i=''.join(i)
#                 check=1
#     if check==1:
#         cnt+=1
# print(cnt)


n = int(input())
words =  [input() for _ in range(n)]
count=0
for word in words:
    buff=[]
    for i, c in enumerate(word):
        if i==0:
            buff.append(c)
        elif c == word[i-1] or c not in buff:
            buff.append(c)
        else: 
            continue
    if len(buff)==len(word):
        count+=1
print(count)