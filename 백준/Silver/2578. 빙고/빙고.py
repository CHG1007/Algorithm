#   빙고  실버 4

# 숫자 체크
def check(num):
    for i in range(5):
        for j in range(5):
            if arr[i][j] == num:
                arr[i][j] = True


# 현재 빙고 줄 개수 반환
def bingo_count():
    cnt = 0

    # 가로
    for i in range(5):
        if all(arr[i][j] == True for j in range(5)):
            cnt += 1

    # 세로
    for i in range(5):
        if all(arr[j][i] == True for j in range(5)):
            cnt += 1

    # 좌상 → 우하 대각선
    if all(arr[i][i] == True for i in range(5)):
        cnt += 1

    # 우상 → 좌하 대각선
    if all(arr[i][4 - i] == True for i in range(5)):
        cnt += 1

    return cnt


# 입력
arr = [list(map(int, input().split())) for _ in range(5)]

call_nums = []
for _ in range(5):
    nums = list(map(int, input().split()))
    call_nums.append(nums)

# 숫자 부르기 진행
count = 0  # 사회자가 숫자를 부른 횟수

for row in call_nums:          # 각 줄(5개 숫자)
    for num in row:            # 각 숫자
        check(num)             # 빙고판에서 체크
        count += 1             # 부른 횟수 증가
        if bingo_count() >= 3: # 빙고 3줄 이상이면 종료
            print(count)
            exit()

