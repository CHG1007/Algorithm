#   5650. [모의 SW 역량테스트] 핀볼 게임


# 방향: 0:상, 1:하, 2:좌, 3:우
DR = (-1, 1, 0, 0)
DC = (0, 0, -1, 1)

# 블록 반사 테이블: 1~5만 사용, 5는 언제나 반대(벽과 동일)
# REFLECT[val][d]: val 블록을 d 방향으로 만나서 변하는 방향
REFLECT = {
    1: [1, 3, 0, 2],
    2: [3, 0, 1, 2],
    3: [2, 0, 3, 1],
    4: [1, 2, 3, 0],
    5: [1, 0, 3, 2],
}


# (sr, sc)에서 방향 d로 출발했을때 얻는 점수 반환 함수
def simulate(sr, sc, d, board, worm_to, N):
    r, c = sr, sc   # 시작 좌표
    score = 0       # 점수

    while True:
        # 한 칸 전진
        r += DR[d]
        c += DC[d]
        val = board[r][c]   # 현재 게임판 좌표의 값

        # 종료 조건 1) 블랙홀
        if val == -1:
            break
        # 종료 조건 2) 출발 위치로 귀환
        if r == sr and c == sc:
            break

        # 블록에 도달 하는 경우 (val: 1~5)
        if 1 <= val <= 5:
            # 블록 반사: 점수 +1, 방향 변경
            d = REFLECT[val][d]
            score += 1
        # 웜홀에 도달 하는 경우 (val: 6~10)
        elif 6 <= val <= 10:
            # 웜홀: 동일 번호의 다른 좌표로 이동(방향 유지)
            nr, nc = worm_to[(r, c)]
            # print(worm_to)
            # 방향과 점수 변화 없음
            r, c = nr, nc
        # 0(빈칸)은 그냥 진행
        else:
            pass

    # 점수 반환
    return score


# 입력 처리
T = int(input().strip())
for tc in range(1, T + 1):
    N = int(input().strip())
    # 바깥을 전부 block 5로 패딩(벽 = 항상 반대 반사)
    board = [[5]*(N+2)] + [[5] + list(map(int, input().split())) + [5] for _ in range(N)] + [[5]*(N+2)]

    # 웜홀 위치 수집: number(6~10) -> [ (r1,c1), (r2,c2) ]
    hole = {}
    for k in range(6, 11):
        hole[k] = []
    # print(hole)
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            v = board[i][j]
            if 6 <= v <= 10:
                # 해당 웜홀 좌표 딕셔너리에 추가
                hole[v].append((i, j))

    # print(hole)
    # 각 웜홀 칸 -> 반대편 웜홀 칸 매핑
    worm_to = {}
    for v in range(6, 11):
        # v 웜홀이 있다면
        if hole[v]:
            (x1, y1), (x2, y2) = hole[v][0], hole[v][1]
            worm_to[(x1, y1)] = (x2, y2)
            worm_to[(x2, y2)] = (x1, y1)
    # print(worm_to)

    ans = 0
    # 모든 빈칸(0)에서 4방향 시뮬레이션
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if board[i][j] != 0:
                continue
            for di in range(4):
                ans = max(ans, simulate(i, j, di, board, worm_to, N))

    # 정답 출력
    print(f"#{tc} {ans}")



