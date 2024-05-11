import sys
input = sys.stdin.readline


n = int(input())
lst = [0] + list(map(int, input().split()))

# dp[i]: i번째를 포함하는 부분 수열 중 합의 최대값(초기값=본인값)
dp = [0]*(n+1)

for i in range(1, n+1):
    # i번째 수보다 전에있는 수들중에 i번째 수보다 크기가 작다면 Sum에 누적합 계산
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j]+lst[i])
        else:
            dp[i] = max(dp[i], lst[i])
        
# print(*lst, sep='\t')
# print(*dp, sep='\t')
print(max(dp))