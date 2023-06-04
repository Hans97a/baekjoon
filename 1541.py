expression = input()
answer = 0

m = expression.split("-")

x = sum(map(int, m[0].split("+")))

if expression[0] == "-":
    answer -= x
else:
    answer += x

for x in m[1:]:
    x = sum(map(int, x.split("+")))
    answer -= x

print(answer)
