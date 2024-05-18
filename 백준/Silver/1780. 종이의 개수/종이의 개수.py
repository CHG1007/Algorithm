import sys
input = sys.stdin.readline


def nine(x, y, N):
    global ans
    third = N//3
    num = arr[x][y]

    for i in range(x, x+N):
        for j in range(y, y+N):
            if num != arr[i][j]:
                for m in range(0, third*2 + 1, third):
                    for n in range(0, third*2 + 1, third):
                        nine(x+m, y+n, third)
                return

    if num == -1:
        ans[0] += 1
    elif num == 0:
        ans[1] += 1
    else:
        ans[2] += 1


N = int(input())    # 행렬의 크기 NxN
arr = [list(map(int, input().split())) for _ in range(N)]   # 행렬 입력
ans = [0]*3

nine(0, 0, N)
print(*ans, sep='\n')