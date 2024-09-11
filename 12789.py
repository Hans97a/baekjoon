from collections import deque

N = int(input())

students = deque(map(int, input().split()))

rest_line = []

for i in range(N):
    if rest_line and rest_line[-1] == i + 1:
        rest_line.pop()
        continue

    while students and students[0] != i + 1:
        rest_line.append(students.popleft())

    if students and students[0] == i + 1:
        students.popleft()
        continue


if not students and not rest_line:
    print("Nice")
else:
    print("Sad")
