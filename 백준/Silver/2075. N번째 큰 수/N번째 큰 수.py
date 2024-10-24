import heapq
import sys
input = sys.stdin.readline


n = int(input())
q = []

for _ in range(n):
    lst = list(map(int, input().split()))
    for num in lst:
        heapq.heappush(q, num)
    while len(q) > n:
        heapq.heappop(q)

print(heapq.heappop(q))