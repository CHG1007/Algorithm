import heapq
from collections import deque
import sys
input = sys.stdin.readline


def box():
    while child:
        gift = child.popleft()
        rest = -q[0] - gift
        if rest >= 0:
            heapq.heappop(q)
            heapq.heappush(q, -rest)
        else:
            return 0
    return 1


n, m = map(int, input().split())
q = list(map(int, input().split()))
child = deque(map(int, input().split()))

q = [-x for x in q]
heapq.heapify(q)
print(box())