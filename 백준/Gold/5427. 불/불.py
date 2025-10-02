from collections import deque
import sys
input = sys.stdin.readline

INF = 10**9
# 4방향(하, 상, 우, 좌)
DR = [(1, 0), (-1, 0), (0, 1), (0, -1)]


# bfs 탐색(불) : 모든 불(*)을 동시에 시작점으로 하여 각 칸에 도달하는 "불의 최단 시간" 계산
def bfs_fire(grid, h, w):
    # 1. 큐, 불 도착시간 배열(초기 INF) 생성
    q = deque()
    fire_time = [[INF] * w for _ in range(h)]

    # 2. 초기 불 좌표들을 큐에 삽입(시간=0), 방문 처리
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '*':
                fire_time[i][j] = 0
                q.append((i, j))

    # 3. BFS (벽은 번지지 않음)
    while q:
        ci, cj = q.popleft()
        for di, dj in DR:
            ni, nj = ci + di, cj + dj
            # 격자 범위, 벽이 아닌 곳, 미도달(=INF)인 곳만
            if 0 <= ni < h and 0 <= nj < w and grid[ni][nj] != '#' and fire_time[ni][nj] == INF:
                fire_time[ni][nj] = fire_time[ci][cj] + 1
                q.append((ni, nj))

    return fire_time


# bfs 탐색(상근) : @에서 시작하여 불보다 "엄격히 먼저" 갈 수 있는 칸만 확장
def bfs_player(grid, fire_time, h, w, si, sj):
    # 1. 시작이 경계면: 1초만에 탈출 (한 칸 움직여 격자 밖으로 나감)
    if si == 0 or si == h - 1 or sj == 0 or sj == w - 1:
        return 1

    # 2. 큐, 상근 도착시간 배열(초기 INF) 생성
    q = deque()
    dist = [[INF] * w for _ in range(h)]

    # 3. 초기값 대입(@ 위치 시간=0), 큐 삽입
    dist[si][sj] = 0
    q.append((si, sj))

    # 4. BFS (한 번 이동할 때마다 시간 +1)
    while q:
        ci, cj = q.popleft()
        t = dist[ci][cj]  # 현재 칸 도착 시간

        for di, dj in DR:
            ni, nj = ci + di, cj + dj

            # 4-1) 격자 밖으로 나가면 즉시 탈출 성공 (현재 시간 + 1초)
            if not (0 <= ni < h and 0 <= nj < w):
                return t + 1

            # 4-2) 이동 가능 조건: 빈칸('.') 이고 미방문(dist==INF)
            if grid[ni][nj] != '.' or dist[ni][nj] != INF:
                continue

            # 4-3) 불보다 "엄격히 먼저" 도착해야 함 (동시는 불가)
            #      다음칸 도착 시간 = t + 1
            if t + 1 < fire_time[ni][nj]:
                dist[ni][nj] = t + 1
                q.append((ni, nj))

    # 5. 모든 경로 시도에도 탈출 실패
    return None


# ---------- 메인 루프 ----------
T = int(input().strip())
for _ in range(T):
    # 1) 입력 처리
    w, h = map(int, input().split())
    grid = [list(input().strip()) for _ in range(h)]

    # 2) 상근 시작 좌표 찾기(@)
    si = sj = -1
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '@':
                si, sj = i, j
                # 상근 위치를 빈칸처럼 취급(상근 이동 로직의 일관성을 위해)
                grid[i][j] = '.'
                break
        if si != -1:
            break

    # 3) 불 BFS로 각 칸의 불 도착 시간 계산
    fire_time = bfs_fire(grid, h, w)

    # 4) 상근 BFS로 탈출 최소 시간 계산
    ans = bfs_player(grid, fire_time, h, w, si, sj)

    # 5) 정답 출력
    print(ans if ans is not None else "IMPOSSIBLE")
