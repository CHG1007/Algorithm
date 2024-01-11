import sys
input = sys.stdin.readline

N = int(input())

arr = []
cnt = 1

for _ in range(N):
    start, end = map(int, input().split())
    arr.append([end, start])

arr.sort()

if N == 1:
    print(cnt)
else:
    last_end = arr[0][0]
    for i in range(1, N):
        if arr[i][1] >= last_end:
            cnt += 1
            last_end = arr[i][0]
    print(cnt)