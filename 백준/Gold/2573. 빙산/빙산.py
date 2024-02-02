from collections import deque
import sys
input = sys.stdin.readline


def solve():
    # 빙하 최대 높이인 10번(년) 동안 반복
    for Year in range(1, 90000):
        cnt = 0
        v = [[0] * M for _ in range(N)]

        # 1. 1년마다 빙하 높이 감소 좌표마다 계산해두기
        for i in range(N):
            for j in range(M):
                if arr[i][j] != 0:
                    year(i, j)

        # 2. 1에서 계산한 높이 만큼 빙하 높이 감소시키기
        for i in range(N):
            for j in range(M):
                if arr2[i][j] > 0:
                    arr[i][j] = max(0, arr[i][j] - arr2[i][j])
                    arr2[i][j] = 0

        # 3. 빙하 몇 덩어리 인지 계산하기
        for i in range(N):
            for j in range(M):
                if arr[i][j] != 0 and v[i][j] == 0:
                    bfs(i, j, v)
                    cnt += 1
                    # 2덩어리 이상이라면 종료
                    if cnt > 1:
                        return Year

        # 4. 다 녹아서 0 덩어리이면 종료
        if cnt == 0:
            return 0


# 1년후 현재 좌표의 빙하 감소 높이 구하는 함수
def year(ci, cj):
    for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni, nj = ci+di, cj+dj
        if arr[ni][nj] == 0:
            arr2[ci][cj] += 1


def bfs(si, sj, v):
    # 1. 큐 생성
    q = deque()

    # 2. 초기데이터 입력
    q.append([si, sj])
    v[si][sj] = 1

    # 3. 4방향 탐색
    while q:
        ci, cj = q.popleft()

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if arr[ni][nj] != 0 and v[ni][nj] == 0:
                v[ni][nj] = 1
                q.append([ni, nj])


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr2 = [[0] * M for _ in range(N)]

print(solve())