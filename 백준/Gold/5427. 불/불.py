#   불   골드 4

from collections import deque
import sys
input = sys.stdin.readline


# bfs 탐색(상근)
def bfs_san(si, sj, fire_time):
    # 만약 시작 위치가 경계라면: 1초만에 탈출(한 칸 움직여 격자 밖으로 나감)
    if si == 0 or si == (h-1) or sj == 0 or sj == (w-1):
        return 1

    # 1. 큐 , 방문 배열(상근 도착시간) 생성
    q = deque()
    san_time = [[INF]*w for _ in range(h)]

    # 2. 초기값 생성, 방문 처리
    san_time[si][sj] = 0
    q.append((si, sj))

    # 3. bfs 탐색
    while q:
        ci, cj = q.popleft()
        c_time = san_time[ci][cj]   # 현재 칸 도착 시간

        if ci == 0 or ci == (h - 1) or cj == 0 or cj == (w - 1):
            return c_time+1

        # 4방향 탐색
        for (di, dj) in ((1, 0), (-1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            # 격자 범위, 방문 여부, 맵 조건
            if 0<=ni<h and 0<=nj<w and san_time[ni][nj] == INF and arr[ni][nj] == '.':
                # 불보다 먼저 도착하는 조건(동시 불가)
                # 다음칸 도착 시간: c_time + 1
                if c_time+1 < fire_time[ni][nj]:
                    san_time[ni][nj] = c_time + 1   # 방문 처리
                    q.append((ni, nj))  # 다음 탐색 좌표 추가

    # 4. 모든 경로 시도에도 탈출 실패
    return None


# bfs 탐색(불): 모든 불(*)에 대해 동시 시작 -> 각 칸의 불의 최단 시간 계산
def bfs_fire():
    # 1. 큐 , 방문 배열(불 도착시간)생성
    q = deque()
    fire_time = [[INF] * w for _ in range(h)]

    # 2. 초기값 생성, 방문 처리
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '*':
                fire_time[i][j] = 0
                q.append((i, j))

    # 3. bfs 탐색
    while q:
        ci, cj = q.popleft()
        # 4방향 탐색
        for (di, dj) in DR:
            ni, nj = ci + di, cj + dj
            # 격자 범위, 방문 여부, 맵 조건
            if 0 <= ni < h and 0 <= nj < w and fire_time[ni][nj] == INF and arr[ni][nj] != '#':
                fire_time[ni][nj] = fire_time[ci][cj] + 1  # 방문 처리
                q.append((ni, nj))  # 다음 탐색 좌표 추가

    return fire_time


# 입력 처리
T = int(input())    # 테스트 케이스 수
INF = 10**9     # 도달 불가
DR = [(-1, 0), (1, 0), (0, -1), (0, 1)]     # 4방향
for _ in range(T):
    # 1) 입력 처리
    w, h = map(int, input().split())    # w: 너비, h: 높이
    arr = [list(input()) for _ in range(h)]     # 맵

    # 2) 상근 시작 좌표 찾기(@)
    si = sj = -1
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '@':
                # 상근 위치
                si, sj = i, j
                # 상근 위치 빈칸 취급
                arr[si][sj] = '.'
                break
        # 상근 위치 찾으면 탈출
        if si != -1:
            break

    # 3) 불 BFS -> 각 칸의 불 도착 시간 계산
    fire_time = bfs_fire()

    # 4) 상근 BFS -> 탈출 최소 시간 계산
    ans = bfs_san(si, sj, fire_time)

    # 5) 정답 출력
    print(ans if ans is not None else "IMPOSSIBLE")


