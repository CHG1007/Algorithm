def cnt(Map):
    ans = 0
    for line in Map:
        s = ''.join(line)
        for slice in s.split('X'):
            if len(slice) >= 2:
                ans += 1
    return ans


n = int(input())

arr = [list(input()) for _ in range(n)]
arr2 = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        arr2[i][j] = arr[j][i]

print(cnt(arr), cnt(arr2))