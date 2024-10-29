import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(ci, cj):
    # 아직 계산 안한경우
    if dp[ci][cj] == -2:
        dp[ci][cj] = 0
        for di, dj in ((-1,0), (1,0), (0,-1), (0,1)):
            pi, pj = ci+di, cj+dj
            if arr[ci][cj] < arr[pi][pj]:
                dp[ci][cj] += dfs(pi, pj)

    return dp[ci][cj]


m, n = map(int, input().split())
# 범위 마킹(0으로 둘러쌈)
arr = [[0]*(n+2)] + [[0]+list(map(int, input().split()))+[0] for _ in range(m)] + [[0]*(n+2)]

# dp 테이블 생성 및 초기화
# dp[i][j] -> (1,1)좌표 에서 해당 좌표까지 가는 경우의 수
dp = [[-2]*(n+2) for _ in range(m+2)]
dp[1][1] = 1

print(dfs(m, n))