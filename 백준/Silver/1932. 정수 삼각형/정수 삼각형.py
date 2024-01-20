import sys
input = sys.stdin.readline

N = int(input())

arr = [[0]] + [[0] + list(map(int, (input().split()))) for _ in range(N)]

# dp[i][j]: i번줄 j번째 까지 오는 경로의 합의 최대값
dp = [[0]*i for i in range(2, N+3)]

for i in range(1, N+1):
    for j in range(1, i+1):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + arr[i][j]

print(max(dp[-1]))