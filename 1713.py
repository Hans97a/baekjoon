N = int(input())
M = int(input())
arr = list(map(int, input().split()))
frame = []
score = []

for i in range(M):
    if arr[i] in frame:
        idx = frame.index(arr[i])
        score[idx] += 1
    else:
        if len(frame) >= N:
            idx = score.index(min(score))
            del frame[idx]
            del score[idx]
        frame.append(arr[i])
        score.append(1)
print(*(sorted(frame)), sep=" ")
