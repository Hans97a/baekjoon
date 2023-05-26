a=input()
if a.isdigit():
    print(int(a)+48)
elif a.isalpha():
    print(ord(a))