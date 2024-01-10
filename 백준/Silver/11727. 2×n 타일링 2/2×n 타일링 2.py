N = int(input())

dp = [0]*(N+1)

if N == 1:
    print(1)
elif N == 2:
    print(3)
else:
    # dp[i] -> 2xi 크기의 직사각형을 채우는 방법의 수
    dp[1] = 1
    dp[2] = 3

    for i in range(3, N+1):
        dp[i] = dp[i-1] + 2*dp[i-2]

    print(dp[N]%10007)