#   수들의 합 2 실버 4


def prefix():
    L = -1
    R = 0
    ans = 0

    for i in range(1, n):
        prefix_lst[i] = lst[i] + prefix_lst[i - 1]

    while R < n:
        total = prefix_lst[R] - prefix_lst[L]
        if L == -1:
            total = prefix_lst[R]
        if total == m:
            ans += 1
            L += 1
        elif total > m:
            L += 1
        elif total < m:
            R += 1

    return ans


# 입력 처리
n, m = map(int, input().split())
lst = list(map(int, input().split()))

prefix_lst = [0]*n
prefix_lst[0] = lst[0]
ans = 0

if n == 1:
    if lst[0] == m:
        ans = 1
else:
    ans = prefix()

print(ans)




