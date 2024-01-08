import sys
import heapq

input = sys.stdin.readline


N = int(input())
q1, q2, ans = [], [], 0

for _ in range(N):
    num = int(input())
    if num < 1:
        heapq.heappush(q1, num)
    elif num > 1:
        heapq.heappush(q2, -num)
    else:
        ans += num

# 음수
while len(q1) > 1:
    n1 = heapq.heappop(q1)
    n2 = heapq.heappop(q1)
    ans += n1*n2
# 양수
while len(q2) > 1:
    n1 = heapq.heappop(q2)
    n2 = heapq.heappop(q2)
    ans += n1*n2

if q1:
    ans += heapq.heappop(q1)
if q2:
    ans -= heapq.heappop(q2)

print(ans)