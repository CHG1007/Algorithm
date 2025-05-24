def bfs(si, sj, ei, ej):
    # 1. 큐 와 방문 배열 생성
    q = []
    v = [[0] * m for _ in range(n)]

    # 2. 큐에 시작 데이터 넣고 방문 표시
    q.append([si, sj])
    v[si][sj] = 1

    while q:
        ci, cj = q.pop(0)
        # 정답 처리
        if (ci, cj) == (ei, ej):
            return v[ei][ej]

        # 4방향 범위내, 조건에 맞으면
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < m and v[ni][nj] == 0 and arr[ni][nj] == 1:
                q.append([ni, nj])
                v[ni][nj] = v[ci][cj] + 1


n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
ans = bfs(0, 0, n-1, m-1)
print(ans)