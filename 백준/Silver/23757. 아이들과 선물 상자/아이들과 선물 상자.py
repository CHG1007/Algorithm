import heapq
import sys
input = sys.stdin.readline


def box():
    for gift in child:
        rest = -heapq.heappop(q) - gift

        if rest > 0:
            heapq.heappush(q, -rest)
        elif rest < 0:
            return 0
    return 1


n, m = map(int, input().split())
q = list(map(int, input().split()))
child = list(map(int, input().split()))

q = [-x for x in q]
heapq.heapify(q)
print(box())