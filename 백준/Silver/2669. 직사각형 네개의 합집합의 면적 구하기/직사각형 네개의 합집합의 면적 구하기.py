arr = [[0]*101 for _ in range(101)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for x in range(x1, x2):
        for y in range(y1, y2):
            arr[x][y] = 1

ans = 0
for i in range(101):
    for j in range(101):
        ans += arr[i][j]

print(ans)