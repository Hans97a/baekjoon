string = input()
user = input()

cnt = 0
table = [False] * len(string)
for i in range(len(string)):
    if string[i] == user[0] and not table[i]:
        check = False
        string_check = string[i : i + len(user)]
        if len(string_check) == len(user):
            for j in range(len(user)):
                if string_check[j] != user[j]:
                    check = True
                    break
            if not check:
                for j in range(i, i + len(user)):
                    table[j] = True
                cnt += 1

print(cnt)
