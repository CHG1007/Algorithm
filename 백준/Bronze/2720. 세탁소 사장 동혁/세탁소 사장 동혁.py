import sys
input = sys.stdin.readline

t = int(input())

coin_ = [25, 10, 5, 1]

for _ in range(t):
    c = int(input())
    ans = []

    for coin in coin_:
        cnt = 0
        cnt += c//coin
        c = c%coin
        ans.append(cnt)

    print(*ans)