user_in = input()
results = []
for i in range(len(user_in) + 1):
    string = user_in[i:]
    if string:
        results.append(string)
results.sort()
print(*results, sep="\n")
