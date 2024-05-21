def solve():
    lst = input()
    stack = []

    for data in lst:
        if data == '(':
            stack.append(data)
        else:
            if len(stack) == 0:
                print('NO')
                return
                stack.pop()
            else:
                stack.pop()

    if len(stack) == 0:
        print('YES')
    else:
        print('NO')


t = int(input())
for _ in range(t):
    solve()