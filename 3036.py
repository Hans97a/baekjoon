N= int(input())
arr=list(map(int, input().split()))

def GCD(num1, num2):
    if num2 == 0:
        return num1
    return GCD(num2, num1%num2)

first= arr[0]

for i in range(1, len(arr)):
    if first > arr[i]:
        gcd=GCD(first, arr[i])
        if first % gcd ==0 and arr[i]% gcd == 0:
            print(f'{first//gcd}/{arr[i]//gcd}')
        else:
            print(f'{first}/{arr[i]}')
    else:
        gcd=GCD(arr[i], first)
        if first % gcd ==0 and arr[i]% gcd == 0:
            print(f'{first//gcd}/{arr[i]//gcd}')
        else:
            print(f'{first}/{arr[i]}')