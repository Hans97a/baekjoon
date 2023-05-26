dial = {'ABC': 3, 'DEF': 4, 'GHI': 5, 'JKL': 6,
        'MNO': 7, 'PQRS': 8, 'TUV': 9, 'WXYZ': 10, }
a = input()
cnt = 0
for i in a:
    for j in list(dial.keys()):
        if i in str(j):
            cnt+=dial[j]
            break
print(cnt)
