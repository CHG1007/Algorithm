t = int(input())
ans = []
for _ in range(t):
    ans.append(int(input()))

MAX = max(ans)
MOD = 10**9+9
dp = [0]*(MAX+1)

if MAX >= 4:
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, MAX+1):
        dp[i] = (dp[i-1] + dp[i-2] + dp[i-3])%MOD
else:
    dp = [0, 1, 2, 4]

for n in ans:
    print(dp[n])