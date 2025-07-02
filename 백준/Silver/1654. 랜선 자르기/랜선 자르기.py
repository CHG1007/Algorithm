#   랜선 자르기  실버 2


def check(mid):
    cnt = 0
    for lan in lst:
        cnt += lan//mid
    # k개 이상 이라면 자르는 크기 키워서 더 확인해보기
    return cnt >= n


# 입력 처리
k, n = map(int, input().split())
lst = [int(input()) for _ in range(k)]


lo = 0
hi = max(lst) + 1

while lo+1 < hi:
    mid = (lo+hi)//2

    if check(mid):
        lo = mid
    else:
        hi = mid

print(lo)

