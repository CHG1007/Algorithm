import sys

input = sys.stdin.readline


# dp[] 테이블 생성 및 포기화
dp = [0] * 12
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 12):
    dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

T = int(input())  # 테스트 케이스 수

for tc in range(T):
    N = int(input())
    print(dp[N])