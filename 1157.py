# import sys
# a = sys.stdin.readline().rstrip().upper()
# al=a[0]
# for i in a:
#     if a.count(al) < a.count(i):
#         al = i
#     elif a.count(al) == a.count(i) and al != i:
#         al = '?'
# print(al)
# a = input().upper()
# al=a[0]
# cnt1=a.count(al)
# for i in a:
#     cnt2=a.count(i)
#     if cnt1 < cnt2:
#         al = i
#         cnt1=a.count(al)
#     elif cnt1 == cnt2 and al != i:
#         al = '?'
# print(al)

a=input().upper()
d={}
for i in a:
    if i not in d:
        d[i]=a.count(i)
cnt=0
al=''
for i in d.keys():
    if d[i]>cnt:
        al=i
        cnt=d[i]
    elif d[i]==cnt:
        al='?'
print(al)
print(d)