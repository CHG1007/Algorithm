import sys

input = sys.stdin.readline


N = int(input())    # 용액의 수
lst = list(map(int, input().split()))   # 용액의 특성값  / 양수라면 산성, 음수라면 알칼리성
Min = 10**10
ans = []    # 합이 0에 근접한 두 용액을 저장할 리스트

lst.sort()

L = 0
R = N-1

while L < R:
    Sum = lst[L] + lst[R]
    if abs(Min) > abs(Sum):
        Min = Sum
        ans = [L, R]

    if Sum > 0:
        R -= 1
    elif Sum < 0:
        L += 1
    else:
        break

print(lst[ans[0]], lst[ans[1]])