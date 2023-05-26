import sys
N=int(sys.stdin.readline())
arr=[ ((sys.stdin.readline()).split()) for i in range(N) ]

temp=sorted(arr, key= lambda x: (int(x[0]), int(x[1])))
for i in range(len(temp)):
    temp[i]= map(int, temp[i])

for i in temp:
    for j in i:
        print(j, end=' ')
    print()