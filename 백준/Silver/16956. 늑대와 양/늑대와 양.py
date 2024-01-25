import sys
input = sys.stdin.readline


def wolf(ci, cj):

    for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni, nj = ci+di, cj+dj
        if 0<=ni<R and 0<=nj<C and arr[ni][nj] == 'W':
            return True

    return False


def wall(ci, cj):
    for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni, nj = ci+di, cj+dj
        if 0<=ni<R and 0<=nj<C and arr[ni][nj] == '.':
            arr[ni][nj] = 'D'


R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]

flag = True

for i in range(R):
    for j in range(C):
        if arr[i][j] == 'S':
            if wolf(i, j):
                flag = False
                break
            else:
                wall(i, j)


if flag:
    print(1)
    for lst in arr:
        row = ''
        for str in lst:
            row += str
        print(row)
else:
    print(0)