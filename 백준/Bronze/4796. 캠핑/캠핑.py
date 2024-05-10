tc = 0

while True:
    ans = 0
    l, p, v = map(int, input().split())
    tc += 1

    if l == 0 and p == 0 and v == 0:
        break

    if v%p >= l:
        ans = l*(v//p) + l
    else:
        ans = l * (v // p) + v % p
    print(f'Case {tc}: {ans}')