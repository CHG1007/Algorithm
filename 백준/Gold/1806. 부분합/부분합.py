def check():
    flag = False
    ans = 10**5 + 1
    L = 0
    R = 0
    Sum = lst[0]

    while L <= R:

        if Sum < s:
            R += 1
            if R >= n:
                break
            Sum += lst[R]
        else:
            flag = True
            ans = min(ans, R-L+1)
            Sum -= lst[L]
            L += 1

    if ans == 10**5 + 1:
        return 0
    else:
        return ans


n, s = map(int, input().split())
lst = list(map(int, input().split()))
print(check())