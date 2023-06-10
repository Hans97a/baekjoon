K = int(input())

for i in range(K):
    arr = list(map(int, input().split()))[1:]
    arr.sort(reverse=True)
    gap = arr[0] - arr[1]

    for j in range(1, len(arr) - 1):
        if arr[j] - arr[j + 1] > gap:
            gap = arr[j] - arr[j + 1]

    print(f"Class {i+1}")
    print(f"Max {arr[0]}, Min {arr[-1]}, Largest gap {gap}")
