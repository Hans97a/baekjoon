import sys


#  호출된 번호를 빙고판에 체크합니다.
def check_bingo(num: str):
    global bingo, checked

    for i in range(5):
        for j in range(5):
            if bingo[i][j] == num:
                checked[i][j] = True
                return


# 빙고의 개수를 확인합니다.
def is_bingo():
    global checked

    bingo_cnt = 0
    # 가로, 세로 빙고 체크
    for i in range(5):
        col_cnt = 0
        row_cnt = 0
        for j in range(5):
            if checked[j][i] == True:
                col_cnt += 1
            if checked[i][j] == True:
                row_cnt += 1

        if col_cnt == 5:
            bingo_cnt += 1
        if row_cnt == 5:
            bingo_cnt += 1

    # 대각선 체크
    left = 0
    right = 0
    for i in range(5):
        if checked[i][i] == True:
            left += 1
        if checked[i][4 - i] == True:
            right += 1

    if left == 5:
        bingo_cnt += 1

    if right == 5:
        bingo_cnt += 1

    if bingo_cnt >= 3:
        return True
    else:
        return False


bingo = []

for _ in range(5):
    bingo.append(list(map(int, input().split())))

announce = []

for _ in range(5):
    announce.append(list(map(int, input().split())))


checked = [[False] * 5 for _ in range(5)]

cnt = 0
for i in range(5):
    for j in range(5):
        cnt += 1
        check_bingo(announce[i][j])
        if is_bingo():
            print(cnt)
            sys.exit()
