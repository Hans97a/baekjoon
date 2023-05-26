R=int(input())
for i in range(R):
    s=input().strip().split()
    for j in s[1]:
        print(j*int(s[0]), end='')
    print()