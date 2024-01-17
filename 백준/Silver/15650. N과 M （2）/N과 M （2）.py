def dfs(n, lst):
    if n == M:
        lst.pop(0)
        ans.append(lst)
        return

    for j in range(1, N+1):
        if v[j] == 0:
            if lst[-1] < j:
                v[j] = 1
                dfs(n+1, lst+[j])
                v[j] = 0


N, M = map(int, input().split())

v = [0]*(N+1)
ans = []

dfs(0, [0])
for lst in ans:
    print(*lst)