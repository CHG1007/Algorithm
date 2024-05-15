from collections import deque


def dfs(si, sj, data):
    global ans
    # 1. 큐 선언
    q = deque()

    # 2. 데이터 삽입, 방문 처리
    q.append([si, sj])
    v[si][sj] = 1

    # 3. 탐색 시작
    while q:
        ci, cj = q.popleft()

        if data == '-':
            for di, dj in ((0, 1), (0, -1)):
                ni, nj = ci + di, cj + dj
                if 0<=ni<n and 0<=nj<m and v[ni][nj] == 0 and arr[ni][nj] == '-':
                    q.append([ni, nj])
                    v[ni][nj] = 1
                    ans -= 1
        else:
            for di, dj in ((1, 0), (-1, 0)):
                ni, nj = ci + di, cj + dj
                if 0<=ni<n and 0<=nj<m and v[ni][nj] == 0 and arr[ni][nj] == '|':
                    q.append([ni, nj])
                    v[ni][nj] = 1
                    ans -= 1


n, m = map(int, (input().split()))

arr = [list(input()) for _ in range(n)]

ans = n*m
v = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if v[i][j] == 0:
            dfs(i, j, arr[i][j])

print(ans)