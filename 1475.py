numbers = "0123456789"
cnt = 1

nums = input()

for num in nums:
    if not num in numbers:
        if num == "6" and "9" in numbers:
            numbers = numbers.replace("9", "", 1)
        elif num == "9" and "6" in numbers:
            numbers = numbers.replace("6", "", 1)
        else:
            cnt += 1
            numbers += "0123456789"
            numbers = numbers.replace(num, "", 1)
    else:
        numbers = numbers.replace(num, "", 1)
print(cnt)
