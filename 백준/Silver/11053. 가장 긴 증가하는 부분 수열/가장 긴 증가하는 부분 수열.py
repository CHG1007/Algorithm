import sys
input = sys.stdin.readline


N = int(input())
lst = [0] + list(map(int, input().split()))

dp = [0]*(N+1)

for i in range(1, N+1):
    Max = 0
    for j in range(i):
        if lst[i] > lst[j]:
            Max = max(Max, dp[j])
    dp[i] = Max + 1

print(max(dp))