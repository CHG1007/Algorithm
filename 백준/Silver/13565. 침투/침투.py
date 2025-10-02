import sys
from collections import deque
input = sys.stdin.readline


# 입력 처리
M, N = map(int, input().split())

arr = [list(input().strip()) for _ in range(M)]

v = [[0]*N for _ in range(M)]
q = deque()

# 1) 시작 지점: 0행의 모든 '0'
for j in range(N):
    if arr[0][j] == '0':
        v[0][j] = 1
        q.append((0, j))

# 2) BFS: 아래쪽 끝(M-1행)에 닿으면 YES
while q:
    ci, cj = q.popleft()
    if ci == M - 1:
        print("YES")
        sys.exit(0)
    # 4방향
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = ci + di, cj + dj
        # 격자 크기, 방문 여부, 격자 맵 조건
        if 0 <= ni < M and 0 <= nj < N and v[ni][nj] == 0 and arr[ni][nj] == '0':
            v[ni][nj] = 1
            q.append((ni, nj))

# 3) 도달 실패 시 NO
print("NO")
