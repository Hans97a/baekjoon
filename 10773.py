k = int(input())
result = []

for i in range(k):
    num = int(input())
    if num == 0 and len(result) > 0:
        result.pop(len(result) - 1)
    else:
        result.append(num)
print(sum(result))
