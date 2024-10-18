import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [] * n

arr.append([0] * m)
for _ in range(n):
    arr.append(list(map(int, input().split())))

k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    ans = 0
    for si in range(i, x+1):
        ans += sum(arr[si][j-1:y])
    print(ans)