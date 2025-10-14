s, d, i, l, n = map(int, input().split())
target = n*4
sum = s+d+i+l
ans = 0
if sum < target:
    ans = target-sum
print(ans)
    