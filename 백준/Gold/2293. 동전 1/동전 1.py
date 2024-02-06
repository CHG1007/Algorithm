N, k = map(int, input().split())

coin_set = set()
for _ in range(N):
    coin_set.add(int(input()))

# dp[i] = i가치의 경우의 수
dp = [0]*(k+1)
dp[0] = 1

for coin in coin_set:
    for j in range(coin, k+1):
        if j-coin >= 0:
            dp[j] += dp[j-coin]

print(dp[k])