import heapq

n = int(input())
heap = []

for _ in range(n):
    a = list(map(int, input().split()))

    if a[0] != 0:
        for gift in a[1:]:
            heapq.heappush(heap, -gift)
    else:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(-1)