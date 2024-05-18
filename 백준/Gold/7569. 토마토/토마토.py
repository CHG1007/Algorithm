from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    # 1. 큐, 방문 배열 생성
    q = deque()
    v = [[[0]*M for _ in range(N)] for _ in range(H)]

    # 2. 초기데이터 삽입, 방문 처리
    cnt = 0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if arr[i][j][k] == 1:
                    q.append([i, j, k])
                    v[i][j][k] = 1
                elif arr[i][j][k] == 0:
                    cnt += 1

    if cnt == 0:
        return 0

    # 3. 탐색
    while q:
        ci, cj, ch = q.popleft()

        for di, dj, dh in ((-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)):
            ni, nj, nh = ci + di, cj + dj, ch + dh
            if 0<=ni<H and 0<=nj<N and 0<=nh<M and v[ni][nj][nh] == 0 and arr[ni][nj][nh] == 0:
                q.append([ni, nj, nh])
                arr[ni][nj][nh] = 1
                v[ni][nj][nh] = v[ci][cj][ch] + 1
                cnt -= 1

    if cnt == 0:
        return v[ci][cj][ch]-1
    else:
        return -1


M, N, H = map(int, input().split())     # 상자의 가로 세로 높이
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

print(bfs())