def solve():
    lst = input()
    stack = []

    for data in lst:
        if data == '(':
            stack.append(data)
        else:
            if stack:
                stack.pop()
            else:
                print('NO')
                return

    if stack:
        print('NO')
    else:
        print('YES')


t = int(input())
for _ in range(t):
    solve()