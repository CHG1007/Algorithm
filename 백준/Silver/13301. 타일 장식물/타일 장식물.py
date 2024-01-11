N = int(input())

if N == 1:
    print(4)
elif N == 2:
    print(6)
else:
    dp = [0]*(N+1)
    dp[1], dp[2] = 1, 1

    for i in range(3, N+1):
        dp[i] = dp[i-1] + dp[i-2]

    dp2 = [0]*(N+1)
    dp2[1], dp2[2] = 4, 6

    for i in range(3, N+1):
        dp2[i] = dp2[i-1] + dp[i]*2

    print(dp2[N])