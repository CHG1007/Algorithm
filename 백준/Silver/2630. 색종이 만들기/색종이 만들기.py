def four(x, y, N):
    global ans_w, ans_b
    half = N//2
    color = arr[x][y]

    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != arr[i][j]:
                four(x, y, half)
                four(x, y+half, half)
                four(x+half, y, half)
                four(x+half, y+half, half)
                return

    if color == 0:
        ans_w += 1
    else:
        ans_b += 1


N = int(input())    # 한 변의 길이
arr = [list(map(int, input().split())) for _ in range(N)]
ans_w, ans_b = 0, 0

four(0, 0, N)
print(ans_w, ans_b)