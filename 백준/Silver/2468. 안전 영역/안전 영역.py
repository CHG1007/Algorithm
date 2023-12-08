from collections import deque
import sys
input = sys.stdin.readline


def bfs(si, sj, e):
    # 1. 큐, 방문 배열 생성
    q = deque()

    # 2. 초기 데이터, 방문처리
    q.append([si, sj])
    v[si][sj] = 1

    # 3. 탐색 및 방문
    while q:
        ci, cj = q.popleft()

        for di, dj in ((-1,0), (1,0), (0,-1), (0,1)):
            ni, nj = ci + di, cj + dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj] == 0 and arr[ni][nj] > e:
                q.append([ni, nj])
                v[ni][nj] = 1


N = int(input())    # 지역의 크기 NxN
arr = [list(map(int, input().split())) for _ in range(N)]   # 지역 입력
ans, high = 0, 0

for i in range(N):
    for j in range(N):
        high = max(high, arr[i][j])

for e in range(high):
    cnt = 0
    v = [[0] * N for _ in range(N)]  # 방문 배열
    for i in range(N):
        for j in range(N):
            if v[i][j] == 0 and arr[i][j] > e:
                bfs(i, j, e)
                cnt += 1
    ans = max(ans, cnt)
print(ans)