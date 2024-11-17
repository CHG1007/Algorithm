#   N번째 큰 수 실버 2

import heapq
import sys
input = sys.stdin.readline


n = int(input())
q = list(map(int, input().split()))     # 길이가 q인 리스트
heapq.heapify(q)    # q는 앞으로 길이가q이고 가장 큰 값들만 저장하는 큐가 됨

# 모든 열에 대해서
for _ in range(n-1):
    lst = list(map(int, input().split()))
    for num in lst:
        # 현재 q에 있는 n개의 값중 가장 작은값보다 큰 값이 있다면
        if num > q[0]:
            heapq.heappop(q)    # q에서 가장 작은값 pop
            heapq.heappush(q, num)  # 현재 더 큰 값인 num은 push
# 현재 q에 있는 n개의 숫자는 전체 n^2개의 숫자중 가장 큰 n개의 값이므로
# heappop(q) >> n^2개의 숫자중 n번째로 큰 숫자 반환
print(heapq.heappop(q))


