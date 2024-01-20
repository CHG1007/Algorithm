import sys
input = sys.stdin.readline


def dfs(n):
    global ans
    if n == N:
        ans += 1
        return

    for j in range(N):
        if not v1[j] and not v2[n+j] and not v3[n-j]:
            v1[j] = True
            v2[n + j] = True
            v3[n - j] = True
            dfs(n+1)
            v1[j] = False
            v2[n + j] = False
            v3[n - j] = False
            
            
N = int(input())
ans = 0

v1 = [False]*N      # 행 검사
v2 = [False]*(2*N)  # 우측 대각선 검사
v3 = [False]*(2*N)  # 좌측 대각선 검사
dfs(0)
print(ans)