def solution(n):
    answer = [[0] * n for _ in range(n)]

    if n == 1:
        return [[1]]

    mode = 1

    x = y = 0

    for i in range(n * n):
        answer[y][x] = i + 1

        if mode % 4 == 1:
            x += 1

            if x == n - 1 or answer[y][x + 1] != 0:
                mode += 1
        elif mode % 4 == 2:
            y += 1

            if y == n - 1 or answer[y + 1][x] != 0:
                mode += 1
        elif mode % 4 == 3:
            x -= 1

            if x == n - 1 or answer[y][x - 1] != 0:
                mode += 1
        else:
            y -= 1
            if y == n - 1 or answer[y - 1][x] != 0:
                mode += 1

    return answer


solution(4)
