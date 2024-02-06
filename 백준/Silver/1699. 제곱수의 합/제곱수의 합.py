N = int(input())

# dp[i]: i를 제곱수의 합으로 나타날 때, 제곱수 항의 최소 개수
dp = [n for n in range(N+1)]

for i in range(1, N+1):
    for j in range(1, int(i**0.5)+1):
        dp[i] = min(dp[i], dp[i-j**2]+1)

print(dp[N])