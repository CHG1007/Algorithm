#   [S/W 문제해결 기본] 2일차 - Ladder2 D4


for _ in range(10):
    tc = int(input())

    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    ans = 0
    min = 100 * 100

    for sj in range(1, 101):
        if arr[0][sj] == 0:
            continue

        cj = sj     # 현재 가로 위치
        ci = 0      # 현재 세로 위치
        cnt = 0     # 움직인 거리
        dr = 0      # 방향 (0: 아래, -1: 왼쪽, 1: 오른쪽)

        while ci < 99:
            cnt += 1
            # 현재 아래 방향 이라면
            if dr == 0:
                ci += 1     # 세로 위치 증가
                # 다음 좌표 왼쪽 탐색
                if arr[ci][cj-1] == 1:
                    dr = -1     # 길이 있다면 방향 >> 왼쪽
                # 다음 좌표 우측 탐색
                elif arr[ci][cj+1] == 1:
                    dr = 1      # 길이 있다면 방향 >> 오른쪽
            # 현재 좌우측 방향 이라면
            else:
                cj += dr
                # 다음 좌표 좌우측 탐색
                if arr[ci][cj+dr] == 0:
                    dr = 0  # 막혀있다면 방향 >> 아래
        # 거리가 기존보다 짧다면
        if cnt <= min:
            min = cnt   # 최단거리 갱신
            ans = sj-1  # 정답 좌표 갱신

    print(f'#{tc} {ans}')


