#   RGB거리 2 골드 4

import sys
input = sys.stdin.readline


# 입력 처리
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]     # 집을 칠하는 비용

# DP 테이블 생성
# dp[i][j]: i번 집까지 j색으로 칠했을때의 최소 비용
dp = [[0]*N for _ in range(3)]
ans = 1e9   # 정답

# dp 실행
for k in range(3):
    for i in range(3):
        dp[i][0] = 1e9

    # 1번 집을 k색으로 고정
    dp[k][0] = arr[0][k]

    # print(*dp, sep='\n')

    for i in range(1, N):
        # 빨간색으로 칠하는 경우
        dp[0][i] = min(dp[1][i-1], dp[2][i-1]) + arr[i][0]
        # 초록색으로 칠하는 경우
        dp[1][i] = min(dp[0][i-1], dp[2][i-1]) + arr[i][1]
        # 파랑색으로 칠하는 경우
        dp[2][i] = min(dp[1][i-1], dp[0][i-1]) + arr[i][2]

    # print(*dp, sep='\n')
    # print('*'*10)
    
    # 최소값 갱신
    # 1번집이 k색 -> N번째 집이 k색인 경우는 제외해야 함
    ans = min(ans, dp[(k+1)%3][N-1], dp[(k+2)%3][N-1])

# 정답 출력
print(ans)


