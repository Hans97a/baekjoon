A, B = input().split()

len_a = len(A)
len_b = len(B)

results = []
for i in range(len_b):
    cnt = 0
    string = B[i : i + len_a]
    l_string = len(string)

    if l_string == len_a:
        for j in range(l_string):
            if string[j] != A[j]:
                cnt += 1
        results.append(cnt)
print(min(results))
