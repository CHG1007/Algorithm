import sys
input = sys.stdin.readline


n, m = map(int, input().split())

dic = {}
ans = n

for _ in range(n):
    keyword = input().rstrip()
    dic[keyword] = 1

for _ in range(m):
    lst = list(input().rstrip().split(','))

    for data in lst:
        if data in dic.keys():
            if dic[data] == 1:
                dic[data] = 0
                ans -= 1
    print(ans)
