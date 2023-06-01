import sys

M = int(sys.stdin.readline())

result = set()
for i in range(M):
    arr = sys.stdin.readline().split()
    if arr[0] == "add":
        result.add(int(arr[1]))
    elif arr[0] == "remove":
        result.discard(int(arr[1]))
    elif arr[0] == "check":
        num = int(arr[1])
        print(1 if num in result else 0)
    elif arr[0] == "toggle":
        num = int(arr[1])
        if num in result:
            result.remove(num)
        else:
            result.add(num)
    elif arr[0] == "all":
        result = {i for i in range(1, 21)}
    else:
        result.clear()
