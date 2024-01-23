N = int(input())

# dp[i]: N자리 이친수의 갯수
dp = [0]*(N+1)
dp[1] = 1

for i in range(2, N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N])