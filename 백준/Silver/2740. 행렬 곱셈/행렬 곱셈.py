n, m = map(int, input().split())
a = []*n    # nxm 행렬
for _ in range(n):
    a.append(list(map(int, input().split())))

m, k = map(int, input().split())
b = []*m    # mxk 행렬
for _ in range(m):
    b.append(list(map(int, input().split())))

arr = []*n  # nxm X mxk -> nxk 행렬

for i in range(n):
    lst = []
    for j in range(k):
        mul = 0
        for x in range(m):
            mul += a[i][x]*b[x][j]
        lst.append(mul)
    arr.append(lst)
for line in arr:
    print(*line)