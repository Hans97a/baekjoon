count = 0
result = None


def recursive(string):
    global count, result

    count += 1
    if result:
        return

    num = 0

    for char in string:
        num += int(char)

    if num >= 10:
        recursive(str(num))
    else:
        if num % 3 == 0:
            result = "YES"
        else:
            result = "NO"


user_input = input()
if len(user_input) != 1:
    recursive(user_input)
    print(count, result, sep="\n")
else:
    print(0, "YES" if int(user_input) % 3 == 0 else "NO", sep="\n")
