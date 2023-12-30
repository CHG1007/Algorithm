from collections import deque

def bfs(si, sj, maps, N, M):
    # 1. 큐, 방문 배열 선언
    q = deque()
    v = [[0] * N for _ in range(M)]
    
    # 2. 초기 데이터
    ans = []
    q.append([si, sj])
    v[si][sj] = 1
    
    # 3. 탐색
    while q:
        ci, cj = q.popleft()
        
        if (ci, cj) == (M-1, N-1):
            ans.append(v[ci][cj])
        
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci + di, cj + dj
            if 0<=ni<M and 0<=nj<N and maps[ni][nj] == 1 and v[ni][nj] == 0:
                q.append([ni, nj])
                v[ni][nj] = v[ci][cj] + 1
    
    if ans:
        return min(ans)
    else:
        return -1
    

def solution(maps):
    N, M = len(maps[0]), len(maps)
    bfs(0, 0, maps, N, M)
    answer = bfs(0, 0, maps, N, M)
    return answer

