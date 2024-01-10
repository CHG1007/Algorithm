N = int(input())

dp2 = [1]*10

for i in range(2, N+1):
    for j in range(10):
        dp2[j] = sum(dp2[j:])

print(sum(dp2)%10007)