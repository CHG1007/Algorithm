import sys
input = sys.stdin.readline


def dfs(pl, mi, mul, div, result, cnt):
    if pl == 0 and mi == 0 and mul == 0 and div == 0:
        ans.append(result)
        return

    if pl > 0:
        dfs(pl-1, mi, mul, div, result + lst[cnt], cnt+1)
    if mi > 0:
        dfs(pl, mi-1, mul, div, result - lst[cnt], cnt + 1)
    if mul > 0:
        dfs(pl, mi, mul-1, div, result * lst[cnt], cnt + 1)
    if div > 0:
        if lst[cnt]*result > 0:
            dfs(pl, mi, mul, div-1, result // lst[cnt], cnt + 1)
        else:
            dfs(pl, mi, mul, div-1, -(result // -lst[cnt]), cnt + 1)


N = int(input())
lst = list(map(int, input().split()))
pl, mi, mul, div = map(int, input().split())

ans = []
Max = -(10**8)
Min = 10**8

dfs(pl, mi, mul, div, lst[0], 1)
print(max(ans))
print(min(ans))