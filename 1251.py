user_in = input()
results = []
for i in range(1, len(user_in)):
    for j in range(i + 1, len(user_in)):
        one = list(user_in[:i])
        two = list(user_in[i:j])
        three = list(user_in[j:])
        one.reverse()
        two.reverse()
        three.reverse()
        string = "".join(one) + "".join(two) + "".join(three)
        results.append(string)
results.sort()
print(results[0])
