def bfs(si, sj):
    # 1. 큐, 방문 배열
    q = []

    # 2. 초기값 입력, 방문 처리
    q.append([si, sj])
    v[si][sj] = 1
    cnt = 1

    while q:
        ci, cj = q.pop(0)
        # 4방향 탐색
        for di, dj in ((-1,0), (1,0), (0,-1), (0,1)):
            ni, nj = ci + di, cj + dj
            # 배열 범위를 벗어나는지, 방문했는지, 방문 가능한 좌표인지 확인
            if 0<=ni<n and 0<=nj<n and v[ni][nj] == 0 and arr[ni][nj] == 1:
                q.append([ni, nj])
                v[ni][nj] = 1
                cnt += 1

    return cnt


n = int(input())    # 지도 크기
arr = [list(map(int, input())) for _ in range(n)]   # 지도 입력
v = [[0]*n for _ in range(n)]   # 방문 배열
ans = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and v[i][j] == 0:
            ans.append(bfs(i, j))

ans.sort()

print(len(ans), *ans, sep='\n')