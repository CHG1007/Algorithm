import heapq
import sys

input = sys.stdin.readline


def dis(q):
    q2 = []
    first = heapq.heappop(q)
    heapq.heappush(q, first)

    while q:
        c = heapq.heappop(q)
        q2.append(min(L-c, c))

    print(max(q2), max(L-first, c))


T = int(input())

for _ in range(T):
    q = []
    L, N = map(int, input().split())

    for _ in range(N):
        heapq.heappush(q, int(input()))

    dis(q)