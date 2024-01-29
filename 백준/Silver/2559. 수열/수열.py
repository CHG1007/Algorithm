N, K = map(int, input().split())
lst = list(map(int, input().split()))

Sum = sum(lst[:K])
ans = [Sum]

for i in range(N-K):
    Sum -= lst[i]
    Sum += lst[i+K]
    ans.append(Sum)

print(max(ans))