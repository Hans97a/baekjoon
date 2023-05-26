N, M = map(int, input().split())
a = []
cnt = 0
arr = []
for i in range(N):
    a.append(input())
WB = 'WBWBWBWB'
BW = 'BWBWBWBW'

for p in range(N-8+1):
    for x in range(M-8+1):
        cntW = 0
        cntB = 0
        for ck, i in enumerate(range(p, p+8)):
            for num, j in enumerate(range(x, x+8)):
                if i == p:
                    
                    if WB[num] != a[i][j]:
                        cntW += 1
                    if BW[num] != a[i][j]:
                        cntB += 1
                    
                else:
                    if ck%2==1:
                        if BW[num] != a[i][j]:
                            cntW += 1
                        if WB[num] != a[i][j]:
                            cntB += 1
                    else:
                        if WB[num] != a[i][j]:
                            cntW += 1
                        if BW[num] != a[i][j]:
                            cntB += 1
        if cntW or cntB:
            if cntW > cntB:
                arr.append(cntB)
            else:
                arr.append(cntW)
                
if len(arr):
    print(min(arr))
else:
    print(0)