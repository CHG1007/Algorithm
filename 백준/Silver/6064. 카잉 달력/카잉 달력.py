import sys
input = sys.stdin.readline


# 정답 반환 함수
def cal(x, y):
    cnt = max(M,N)
    
    if M > N:
        k = x
    else:
        k = y
    while k <= M*N:
        if (k-x)%M == 0 and (k-y)%N == 0:
            return k
        k += cnt

    return -1

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    print(cal(x, y))