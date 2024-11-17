#   N과 M (3)    실버 3


def dfs(n, tlst):
    # print(n, tlst)
    if n == m:
        ans.append(tlst)
        return

    for j in range(1, N+1):
        dfs(n+1, tlst+[j])


N, m = map(int, input().split())
ans = []
dfs(0, [])
for lst in ans:
    print(*lst)
