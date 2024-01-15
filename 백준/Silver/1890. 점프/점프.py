import sys
input = sys.stdin.readline

N = int(input())
arr = [[0]*(N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(N+1) for _ in range(N+1)]
dp[1][1] = 1

for i in range(1, N+1):
    for j in range(1, N+1):
        if dp[i][j] != 0 and arr[i][j] != 0:
            if i+arr[i][j] <= N:
                dp[i+arr[i][j]][j] += dp[i][j]
            if j + arr[i][j] <= N:
                dp[i][j+arr[i][j]] += dp[i][j]

print(dp[N][N])