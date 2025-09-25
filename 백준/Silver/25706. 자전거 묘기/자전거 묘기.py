#   자전거 묘기 실버 3

import sys
input = sys.stdin.readline

# 입력 처리
N = int(input())    # N: 도로의 길이
lst = [0] + list(map(int, input().split())) + [0]*N       # 도로의 상태

# dp 테이블 생성
dp = [0]*(2*N+1)
dp[N] = 1

# dp 테이블 N번째 칸 부터 1번째 칸으로 뒤에서 부터 계산
# dp[i]: i번째 칸에서 시작해 자전거를 타고 밟는 총 칸의 개수
for i in range(N-1, 0, -1):
    dp[i] = dp[i+lst[i]+1] + 1

# 정답 출력
print(*dp[1:N+1])


