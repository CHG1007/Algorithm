#   N과 M (2)    실버 3


def dfs(n, cnt, tlst):
    if n > N:
        if cnt == m:
            ans.append(tlst)
        return

    dfs(n+1, cnt+1, tlst+[n])   # 선택하는 경우
    dfs(n+1, cnt, tlst)         # 선택하지 않는 경우


N, m = map(int, input().split())

ans = []
dfs(1, 0, [])
for lst in ans:
    print(*lst)
