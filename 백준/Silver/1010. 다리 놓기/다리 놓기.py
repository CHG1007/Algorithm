import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    lst = list(range(1, M+1))

    dp = [0]*(M+1)
    dp[N] = 1

    for i in range(N+1, M+1):
        dp[i] = (dp[i-1]*i)//(i-N)

    print(dp[M])