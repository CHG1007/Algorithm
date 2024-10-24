import heapq
import sys
input = sys.stdin.readline


n = int(input())
q_p, q_n = [], []

for _ in range(n):
    x = int(input())

    if x != 0:
        if x > 0:
            heapq.heappush(q_p, x)
        else:
            heapq.heappush(q_n, -x)
    else:
        if q_p and q_n:
            tmp_p = heapq.heappop(q_p)
            tmp_n = heapq.heappop(q_n)

            if tmp_n <= tmp_p:
                print(-tmp_n)
                heapq.heappush(q_p, tmp_p)
            else:
                print(tmp_p)
                heapq.heappush(q_n, tmp_n)
        elif q_p and not q_n:
            print(heapq.heappop(q_p))
        elif not q_p and q_n:
            print(-heapq.heappop(q_n))
        else:
            print(0)