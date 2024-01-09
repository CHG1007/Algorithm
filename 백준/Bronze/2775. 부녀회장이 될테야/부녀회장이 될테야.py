import sys

input = sys.stdin.readline

dp = [[0]*15 for _ in range(15)]

for i in range(15):
    dp[0][i] = i+1

for i in range(1, 15):
    for j in range(15):
        for k in range(j+1):
            dp[i][j] += dp[i-1][k]


T = int(input())

for _ in range(T):
    K = int(input())
    N = int(input())

    print(dp[K][N-1])