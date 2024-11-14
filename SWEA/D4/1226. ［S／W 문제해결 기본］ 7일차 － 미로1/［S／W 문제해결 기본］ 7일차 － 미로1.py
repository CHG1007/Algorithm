def bfs(si, sj):
    # 1. 큐와 방문 배열 생성
    q = []
    v = [[0]*N for _ in range(N)]

    # 2. 큐에 초기데이터 삽입, v 표시
    q.append([si, sj])
    v[si][sj] = 1

    while q:
        ci, cj = q.pop(0)
        if arr[ci][cj] == 3:
            return v[ci][cj]

        # 네방향, 범위내, 미방문, 벽이 아니면 방문(q)
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci +di, cj + dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj] != 1:
                q.append([ni, nj])
                v[ni][nj] = 1

    return 0


def dfs(ci, cj):
    # 네방향, 범위내, 미방문, 벽이 아니면 방문(q)
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = ci + di, cj + dj
        if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and arr[ni][nj] != 1:
            v[ni][nj] = 1
            dfs(ni, nj)


for tc in range(10):
    t = int(input())
    N = 16
    arr = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                si, sj = i, j
            if arr[i][j] == 3:
                ei, ej = i, j

    # 1. bfs
    # ans = bfs(si, sj)
    # print(f'#{t} {ans}')

    # 2. dfs
    v = [[0]*N for _ in range(N)]
    v[si][sj] = 1
    dfs(si, sj)
    print(f'#{t} {v[ei][ej]}')