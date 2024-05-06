import sys
input = sys.stdin.readline

n = int(input())

lst = []
for _ in range(n):
    lst.append(int(input()))
lst.sort(reverse=True)

dp = [0]*(n+1)
dp[1] = lst[0]

for i in range(n):
    dp[i+1] = lst[i]*(i+1)

print(max(dp))