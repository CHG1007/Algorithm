#   세로읽기    브론즈 1


arr = []
len_Max = 0
for _ in range(5):
    s = list(input())
    arr.append(s)
    len_Max = max(len_Max, len(s))

for i in range(len_Max):
    for j in range(5):
        if len(arr[j]) > i:
            print(*arr[j][i], end='')



