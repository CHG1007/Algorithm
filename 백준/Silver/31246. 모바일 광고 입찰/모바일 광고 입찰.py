import sys
from collections import deque
input = sys.stdin.readline


N, K = map(int, input().split())
arr = []

for _ in range(N):
    A, B = map(int, input().split())
    arr.append(A-B)

arr.sort(reverse=True)
arr = deque(arr)
cnt, price = 0, 0
while arr:
    first = arr.popleft()
    if first+price >= 0:
        cnt += 1
    else:
        arr.appendleft(first)
        price = (-1)*first
    if cnt >= K:
        break

print(price)