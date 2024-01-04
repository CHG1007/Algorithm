import sys

input = sys.stdin.readline

n = int(input())    # n번째 피보나치 수

dp = [0]*(n+1)
dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[n])