import sys
N=int(sys.stdin.readline())
arr= [ list(map(int, sys.stdin.readline().split())) for i in range(N)]
arr=sorted(arr, key= lambda x: (x[1], x[0]))

for i in arr:
    for j in i:
        print(j, end=' ')
    print()
    


