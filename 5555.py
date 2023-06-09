find_str = input()
N = int(input())


cnt = 0

for _ in range(N):
    ring = input()
    ring_len = len(ring)
    for i in range(ring_len):
        string = ""
        check = False
        for j in range(ring_len):
            idx = (i + j) % ring_len
            string += ring[idx]

            if len(find_str) == len(string):
                if string == find_str:
                    cnt += 1
                    check = True
                break
        if check:
            break

print(cnt)
