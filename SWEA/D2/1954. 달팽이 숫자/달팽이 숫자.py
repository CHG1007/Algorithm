#   달팽이 숫자 D2

t = int(input())

for tc in range(t):
    n = int(input())

    # nxn 배열
    arr = [[0]*n for _ in range(n)]

    num = 1             # 채울 숫자
    arr[0][0] = num     # 초기값
    ci, cj = 0, 0       # 현재 좌표
    num += 1           

    # 시계 방향 4방향
    dr = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # 방향 초기값
    dr_n = 0

    # 마지막 칸인 n^2 이 될때까지
    while num <= n**2:
        di, dj = dr[dr_n][0], dr[dr_n][1]
        ni, nj = ci+di, cj+dj
        # 아직 방문하지 않았고 배열 범위 안이라면
        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 0:
            arr[ni][nj] = num   # 숫자 채우기
            ci, cj = ni, nj     # 다음칸 좌표
            num += 1            # 채울 숫자 증가
        # 벗어나면 방향 전환
        else:
            dr_n = (dr_n+1)%4

    print(f'#{tc+1}')
    for lst in arr:
        print(*lst)
