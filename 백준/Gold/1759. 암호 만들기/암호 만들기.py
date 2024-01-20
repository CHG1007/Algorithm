import sys
input = sys.stdin.readline


def dfs(n, s, tlst):
    cnt = 0
    if n == L:
        if 'a' in tlst:
            cnt += 1
        if 'e' in tlst:
            cnt += 1
        if 'i' in tlst:
            cnt += 1
        if 'o' in tlst:
            cnt += 1
        if 'u' in tlst:
            cnt += 1

        if 1 <= cnt <= L-2:
            ans.append(tlst)
        return

    for i in range(s, len(lst)):
        if not v[i]:
            v[i] = True
            dfs(n+1, i, tlst + [lst[i]])
            v[i] = False


L, C = map(int, input().split())
lst = list(input().split())

ans = []
v = [False]*C
# 문자열 정렬
lst.sort()

dfs(0, 0, [])
for lst in ans:
    print(*lst, sep='')