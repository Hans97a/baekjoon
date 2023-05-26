from collections import Counter
N=int(input())
cards=list(map(int, input().split()))
M=int(input())
given=list(map(int, input().split()))
cnt=Counter(cards)
for i in given:
    print(cnt[i], end=' ')