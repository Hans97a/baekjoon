def GCD(a, b):
    if a % b == 0:
        return b
    return GCD(b, a % b)


user_in = input()
A, B = map(int, user_in.split(":"))


if A > B:
    div = GCD(A, B)
else:
    div = GCD(B, A)
print(f"{A//div}:{B//div}")
