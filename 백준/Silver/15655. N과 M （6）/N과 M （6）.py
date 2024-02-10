def dfs(n, s, tlst):
    if n==M:
        ans.append(tlst)
        return

    for j in range(s, N):   # 오름차순 수열을 위해서 선택한 숫자 이후 값부터 선택
        if v[j]==0:
            v[j]=1
            dfs(n+1, j+1, tlst+[lst[j]])
            v[j]=0

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))

ans = []
v = [0]*N
# 선택개수, 시작j위치, tlst
dfs(0, 0, [])

for lst in ans:
    print(*lst)