import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))

# dp[i]: i번째 숫자까지의 합
dp = [0]*(N+1)
dp[1] = lst[0]

if N > 1:
    for i in range(2, N+1):
        dp[i] = dp[i-1] + lst[i-1]

for _ in range(M):
    i, j = map(int, input().split())
    print(dp[j]-dp[i-1])