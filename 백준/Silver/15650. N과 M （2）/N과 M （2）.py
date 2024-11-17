#   N과 M (2)    실버 3


def dfs(n, s, lst):
    if n == M:
        ans.append(lst)
        return

    for j in range(s, N+1):
        dfs(n+1, j+1, lst+[j])


N, M = map(int, input().split())
ans = []

dfs(0, 1, [])

for lst in ans:
    print(*lst)
