N = int(input())

# dp[i]: 길이가 N일때 타일의 모든 가짓수
dp = [0]*(N+1)
dp[0], dp[1] = 1, 1

# 직전 타일 뒤에 '1' 타일 , 전전 타일 뒤에 '00'타일
for i in range(2, N+1):
    dp[i] = (dp[i-1] + dp[i-2])%15746

print(dp[N])