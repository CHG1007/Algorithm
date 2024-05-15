def bfs(si, sj):
    #   1. 큐, 방문 배열 선언
    q = []
    cnt = 1

    # 2. 초기값 대입, 방문처리
    q.append([si, sj])
    v[si][sj] = 1
    w = 0

    while q:
        ci, cj = q.pop(0)
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0<=ni<n and 0<=nj<m and v[ni][nj] == 0 and arr[ni][nj] == 1:
                cnt += 1
                q.append([ni, nj])
                v[ni][nj] = 1
    return cnt


n, m = map(int, input().split())    # 세로, 가로
arr = [list(map(int, input().split())) for _ in range(n)]   # 도화지
ans = []

v = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and v[i][j] == 0:
            ans.append(bfs(i, j))

if len(ans)==0:
    print(len(ans))
    print(0)
else:
    print(len(ans))
    print(max(ans))