n = int(input())

target = [int(input()) for _ in range(n)]


def sol():
    stack = [1]
    cur = 2
    result = ["+"]

    for num in target:
        while cur <= num:
            stack.append(cur)
            cur += 1
            result.append("+")
        if stack.pop() != num:
            return "NO"
        result.append("-")

    return "\n".join(result)


print(sol())
