import sys
input = sys.stdin.readline

N = int(input())
lst = [0] + list(map(int, input().split()))

# dp[i]: i개의 카드를 구매하기 위해 지불하는 금액의 최댓값
dp = [0]*(N+1)
dp[1] = lst[1]

if N > 1:
    for i in range(2, N+1):
        tmp = 0
        for j in range(1, i):
            tmp = max(tmp, dp[i-j]+dp[j])
        dp[i] = max(tmp, lst[i])

print(dp[N])