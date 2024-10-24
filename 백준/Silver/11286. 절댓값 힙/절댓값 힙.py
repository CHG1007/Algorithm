import heapq
import sys
input = sys.stdin.readline


n = int(input())
q_p, q_n = [], []   # 양수 힙, 음수 힙

for _ in range(n):
    x = int(input())

    if x != 0:
        if x > 0:
            heapq.heappush(q_p, x)
        else:
            heapq.heappush(q_n, -x)
    else:
        # 양수, 음수 힙 모두 존재 -> 최소값비교후 더 작은값 pop
        if q_p and q_n:
            if q_n[0] <= q_p[0]:
                print(-heapq.heappop(q_n))
            else:
                print(heapq.heappop(q_p))
        # 양수 힙만 존재 -> 양수 힙 pop
        elif q_p and not q_n:
            print(heapq.heappop(q_p))
        # 음수 힙만 존재 -> 음수 힙 pop
        elif not q_p and q_n:
            print(-heapq.heappop(q_n))
        else:
            print(0)