N = int(input())

dp = [4]*(N+1)
dp[0] = 0

M = int(N**0.5)
for i in range(1, M+1):
    for j in range(i**2, N+1):
        dp[j] = min(dp[j-i**2]+1, dp[j])

print(dp[N])