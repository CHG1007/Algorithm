import sys
input = sys.stdin.readline


left = list(input().rstrip())
N = int(input())
order = [input().split() for _ in range(N)]

right = []


for menu in order:
    if menu[0] == 'L':
        if left:
            right.append(left.pop())
    elif menu[0] == 'D':
        if right:
            left.append(right.pop())
    elif menu[0] == 'B':
        if left:
            left.pop()
    else:
        left.append(menu[1])

print(*left, *right[::-1], sep='')