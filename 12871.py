s = input()
t = input()

if len(s) > len(t):
    s, t = t, s

s_len = len(s)
t_len = len(t)
i = t_len
while True:
    if i % s_len == 0 and i % t_len == 0:
        break
    i += 1

if s * (i // s_len) == t * (i // t_len):
    print(1)
else:
    print(0)
