while True:
    try:
        user_in = input()
    except:
        break

    substr, mainstr = user_in.split()

    idx = 0
    check = False

    for i in range(len(mainstr)):
        if mainstr[i] == substr[idx]:
            idx += 1

            if idx == len(substr):
                check = True
                break
    print("Yes" if check else "No")
