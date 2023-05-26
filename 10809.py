#my
# a=input()
# b='abcdefghijklmnopqrstuvwxyz'  ==string임포트하고 string.ascii_lowercase로 하면 간단
# for i in b:
#     if i in a:
#         print(a.index(i), end=' ')
#     else:
#         print(-1, end=' ')
#other
w=input()
a=list(range(97,123))
for i in a:print(w.find(chr(i)),end=' ')