t = int(input())

for _ in range(t):
    ans = []
    tc = int(input())

    lst = list(map(int, input().split()))
    set_lst = set(lst)

    for num in set_lst:
        ans.append([lst.count(num), num])

    ans.sort(key=lambda x: (-x[0], -x[1]))
    print(f'#{tc} {ans[0][1]}')