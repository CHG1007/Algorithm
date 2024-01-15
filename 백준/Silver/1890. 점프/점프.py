import sys
input = sys.stdin.readline

N = int(input())
arr = [[0]*(N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

# dp[i][j] -> (1,1)에서 시작하여 (i,j)로 오는 경로 수
dp = [[0]*(N+1) for _ in range(N+1)]
dp[1][1] = 1

for i in range(1, N+1):
    for j in range(1, N+1):
        # 시작점부터 갈수있는 위치만 탐색
        if dp[i][j] != 0 and arr[i][j] != 0:
            jump = arr[i][j]
            
            # 행 범위 내라면 -> 아래 이동
            if i+jump <= N:
                dp[i+jump][j] += dp[i][j]
            # 열 범위 내라면 -> 우측 이동
            if j + arr[i][j] <= N:
                dp[i][j+jump] += dp[i][j]

print(dp[N][N])