import sys

a=int(sys.stdin.readline().rstrip())
for i in range(a):
    A=sys.stdin.readline().rstrip().split()
    tempA, tempB=map(int, A)
    print(tempA + tempB)