#   행렬 덧셈   브론즈 3


n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

arr = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        arr[i][j] = a[i][j]+b[i][j]

for line in arr:
    print(*line)