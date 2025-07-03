#   두 수의 합  실버 3


# 입력 처리
n = int(input())
lst = list(map(int, input().split()))
x = int(input())

ans = 0
lst.sort()
L = 0
R = n-1

while L < R:
    # 합이 x보다 작다면
    if lst[L]+lst[R] < x:
        L += 1
    # 합이 x보다 크다면
    elif lst[L]+lst[R] > x:
        R -= 1
    # 합이 x라면
    else:
        ans += 1
        L += 1

print(ans)
