alphabet=['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
a=input()

for char in alphabet:
    if char in a:
        a=a.replace(char, 'a')
print(len(a))