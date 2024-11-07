import sys
input = sys.stdin.readline


def search():
    start = m//n
    end = max(lst)

    while start <= end:
        mid = (start+end)//2

        if check(mid) > 0:
            start = mid+1
        elif check(mid) == 0:
            return mid
        else:
            end = mid-1

    if check(mid) < 0:
        return mid-1
    else:
        return mid


def check(num):
    rest = m
    for data in lst:
        if data >= num:
            rest -= num
        else:
            rest -= data
    return rest


n = int(input())
lst = list(map(int, input().split()))
m = int(input())

ans = search()
print(ans)
