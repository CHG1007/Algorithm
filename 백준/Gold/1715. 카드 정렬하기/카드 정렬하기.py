
import heapq
import sys

input = sys.stdin.readline

N = int(input())
q = []
ans = 0

for _ in range(N):
   heapq.heappush(q, int(input()))

while len(q) > 1:
    c1 = heapq.heappop(q)
    c2 = heapq.heappop(q)
    ans += c1+c2
    heapq.heappush(q, c1+c2)

print(ans)