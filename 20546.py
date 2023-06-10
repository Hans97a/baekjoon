cash1 = cash2 = int(input())
stock1 = stock2 = 0
prices = list(map(int, input().split()))

for price in prices:
    if cash1 >= price:
        stock1 = cash1 // price
        cash1 = cash1 % price


upcheck = downcheck = 0
price = prices[0]
for i in range(1, len(prices) - 1):
    if prices[i] > price:
        upcheck += 1
        downcheck = 0
    elif prices[i] < price:
        downcheck += 1
        upcheck = 0
    else:
        upcheck = downcheck = 0
    price = prices[i]

    if upcheck >= 3:
        if stock2:
            cash2 = stock2 * price
            stock2 = 0
    elif downcheck >= 3:
        if cash2 >= price:
            stock2 += cash2 // price
            cash2 = cash2 % price
result1 = cash1 + stock1 * prices[-1]
result2 = cash2 + stock2 * prices[-1]
if result1 > result2:
    print("BNP")
elif result1 < result2:
    print("TIMING")
else:
    print("SAMESAME")
