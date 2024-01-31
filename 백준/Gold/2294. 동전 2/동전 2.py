import sys
input = sys.stdin.readline


N, K = map(int, input().split())
sset = set()        # 동전 중복 제거
for _ in range(N):
    sset.add(int(input()))

# dp[i]: i가치를 만드는 동전의 최소 개수
INF = K+1
dp = [INF]*(K+1)
dp[0] = 0

for coin in sset:
    for j in range(1, K+1):
        if j-coin >= 0:
            dp[j] = min(dp[j], dp[j-coin]+1)

ans = dp[K]
if ans == INF:
    ans = -1
print(ans)