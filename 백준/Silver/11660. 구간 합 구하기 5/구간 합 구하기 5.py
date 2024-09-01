#   구간 합 구하기 5  실버 1

import sys

input = sys.stdin.readline

n, m = map(int, input().split())    # 표의 크기, 합 구하는 횟수

arr = [list(map(int, input().split())) for _ in range(n)] + [[0]*n]
# 표

lst = [list(map(int, input().split())) for _ in range(m)]
# (x1, y1) (x2, y2) 좌표값들

dp = [[0]*n for _ in range(n+1)]    # 누적합 표
dp[0][0] = arr[0][0]                # 초기값


for i in range(n):
    for j in range(1, n):
        dp[i][j] = dp[i][j-1] + arr[i][j]   # 누적합 계산
    dp[i+1][0] = dp[i][-1] + arr[i+1][0]    # 열 첫번째 값 초기값

# m개 (x1, y1) (x2, y2)에 대해
for i in range(m):
    ans = 0 # 정답
    x1, y1, x2, y2 = lst[i]
    
    # 종료열-시작열 횟수만큼 열 누적합 계산
    for j in range(x2-x1+1):
        if y1 == 1:
            if j + x1-1 == 0:
                ans += dp[j + x1-1][y2-1]
            else:
                ans += dp[j + x1 - 1][y2 - 1] - dp[j + x1-1-1][-1]
        else:
            ans += dp[j + x1-1][y2-1] - dp[j + x1-1][y1-1 - 1]
    print(ans)
