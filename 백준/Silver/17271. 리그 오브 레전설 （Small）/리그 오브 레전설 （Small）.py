n, m = map(int, input().split())

dp = [0]*(n+1)

if m<=n:
    for i in range(1, m+1):
        dp[i] = 1
    dp[m] += 1

    for i in range(m+1, n+1):
        dp[i] = (dp[i-1] + dp[i-m])%1000000007

    print(dp[-1])
else:
    print(1)