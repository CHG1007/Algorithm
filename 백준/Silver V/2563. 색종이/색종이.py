import sys
input = sys.stdin.readline

N = int(input())
lst = []

for _ in range(N):
    lst.append(list(map(int, input().split())))

arr = [[0]*100 for _ in range(100)]

for (x, y) in lst:
    for i in range(x, x+10):
        for j in range(y, y+10):
            if arr[i][j] == 1:
                pass
            arr[i][j] = 1

ans = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            ans += 1

print(ans)