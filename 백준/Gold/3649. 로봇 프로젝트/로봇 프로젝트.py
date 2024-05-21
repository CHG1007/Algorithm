import sys


def solve(target):
    L, R = 0, n-1
    while L < R:
        Sum = lst[L] + lst[R]

        if Sum == target:
            print(f'yes {lst[L]} {lst[R]}')
            return
        elif Sum > target:
            R -= 1
        else:
            L += 1

    print('danger')


input = sys.stdin.readline

while True:
    try:
        x = int(input())
        n = int(input())

        lst = []
        for _ in range(n):
            lst.append(int(input()))
        lst.sort()

        solve(x*10**7)

    except:
        break