import sys

input = sys.stdin.readline

dp = [0]*1001
dp[0] = 0
dp[1] = 1
dp[2] = 2

for i in range(3, 1001):
    dp[i] = dp[i-1] + dp[i-2]

N = int(input())

print(dp[N]%10007)