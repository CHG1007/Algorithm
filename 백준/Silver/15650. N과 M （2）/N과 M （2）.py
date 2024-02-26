def dfs(n, lst):
    if n > N:
        if len(lst) == M:
            ans.append(lst)
        return

    dfs(n+1, lst+[n])
    dfs(n+1, lst)


N, M = map(int, input().split())
ans = []

dfs(1, [])

for lst in ans:
    print(*lst)