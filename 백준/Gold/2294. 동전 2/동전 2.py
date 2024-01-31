import sys
input = sys.stdin.readline


N, K = map(int, input().split())
lst = sorted(list(set([int(input()) for _ in range(N)])))

# dp[i]: i가치를 만드는 동전의 최소 개수
dp = [0]*(10**7+1)
for num in lst:
    dp[num] = 1

for i in range(lst[0]+1, K+1):
    tlst = []
    for j in lst:
        if i-j >= 0 and dp[i-j] != 0:
            tlst.append(dp[i-j])
    if tlst:
        if dp[i] != 1:
            dp[i] = min(tlst)+1

if dp[K] == 0:
    print(-1)
else:
    print(dp[K])