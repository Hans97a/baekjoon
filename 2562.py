a = []
for i in range(9):
    a.append(input())
N = 0
max = 0
for i in range(len(a)):
    if max < int(a[i]):
        N = i+1
        max = int(a[i])
print(max, N)


# 다른사람꺼
# A = []

# for i in range(9):
# 	A.append(int(input()))

# print(max(A))
# print(A.index(max(A))+1)