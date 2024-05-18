n = int(input())
m = int(input())
lst = list(map(int, input().split()))

lst.sort()

L = 0
R = n-1
ans = 0

while L < R:
    Sum = lst[L]+lst[R]

    if Sum < m:
        L += 1
    elif Sum > m:
        R -= 1
    else:
        ans += 1
        L += 1

print(ans)