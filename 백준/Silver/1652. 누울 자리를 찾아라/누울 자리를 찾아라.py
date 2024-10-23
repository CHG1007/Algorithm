def col(Map):
    ans = 0
    for line in Map:
        cnt = 0
        for i in range(len(line)):
            if line[i] == '.':
                cnt += 1
            else:
                cnt = 0
            if cnt == 2:
                ans += 1
    return ans


n = int(input())

arr = [list(input()) for _ in range(n)]
arr2 = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        arr2[i][j] = arr[j][i]

print(col(arr), col(arr2))