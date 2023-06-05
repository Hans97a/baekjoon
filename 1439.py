S = input()

zero_cnt = 0
one_cnt = 0

s = S[:1]
if s == "0":
    zero_cnt += 1
else:
    one_cnt += 1

for char in S:
    if char != s[0]:
        s = char
    else:
        continue

    if s == "0":
        zero_cnt += 1
    else:
        one_cnt += 1
print(min(zero_cnt, one_cnt))
