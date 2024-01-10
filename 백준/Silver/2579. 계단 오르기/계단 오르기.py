import sys

input = sys.stdin.readline

N = int(input())
q = []

for _ in range(N):
    q.append(int(input()))

if N == 1:
    print(q[0])
else:
    dp = [[0]*(N+1) for _ in range(3)]

    dp[0][1] = 0
    dp[1][1] = q[0]
    dp[2][1] = 0

    for i in range(2, N+1):
        dp[0][i] = max(dp[1][i-1], dp[2][i-1])
        dp[1][i] = dp[0][i-1] + q[i-1]
        dp[2][i] = dp[1][i-1] + q[i-1]

    print(max(dp[1][N], dp[2][N]))