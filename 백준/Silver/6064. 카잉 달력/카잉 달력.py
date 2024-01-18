import sys
input = sys.stdin.readline


# 정답 반환 함수
def cal(x, y):
    k = x
    while k <= M*N:
        if (k-y)%N == 0:
            return k
        k += M

    return -1


T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    print(cal(x, y))