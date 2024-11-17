#   N과 M (6)    실버 3


def dfs(n, s, tlst):
    if n == m:
        ans.append(tlst)
        return

    for j in range(s, N):
        if v[j] == 0:
            v[j] = 1
            dfs(n+1, j+1, tlst+[lst[j]])
            v[j] = 0


N, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

ans = []
v = [0]*N
dfs(0, 0, [])

for lst in ans:
    print(*lst)
