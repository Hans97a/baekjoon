def GCD(num1, num2):
    if num2==0:
        return num1
    return GCD(num2, num1%num2)

def lcm(num1, num2):
    G= GCD(num1, num2)
    return (num1*num2)//G

T=int(input())

for i in range(T):
    a, b = map(int, input().split())
    print(lcm(a, b))