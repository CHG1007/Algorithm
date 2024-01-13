import heapq
import sys

input = sys.stdin.readline


def dis(q, L):
    q2 = []
    first = heapq.heappop(q)
    heapq.heappush(q, first)

    while q:
        c = heapq.heappop(q)
        heapq.heappush(q2, min(L-c, c))

    while q2:
        long = heapq.heappop(q2)
        
    print(long, max(L-first, c))


T = int(input())

for _ in range(T):
    q = []
    L, N = map(int, input().split())

    for _ in range(N):
        heapq.heappush(q, int(input()))

    dis(q, L)