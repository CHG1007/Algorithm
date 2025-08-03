#   중앙값 구하기 골드 2


import sys
import heapq
input = sys.stdin.readline

t = int(input())  # 테스트 케이스 개수

for _ in range(t):
    m = int(input())  # 이번 케이스의 수열 길이
    nums = []

    # 입력은 10개씩 끊어져 들어오기 때문에 전체 길이가 m이 될 때까지 확장
    while len(nums) < m:
        nums.extend(map(int, input().split()))

    # left: 최대힙(중앙값 이하 값 저장, 음수로 저장해서 최대힙처럼 사용)
    # right: 최소힙(중앙값 초과 값 저장)
    left, right = [], []
    res = []  # 중앙값을 저장할 리스트

    for i, num in enumerate(nums):
        # 1. 새 값은 일단 left(최대힙)에 삽입
        #    heapq는 최소힙이므로 음수로 저장해서 최대힙처럼 사용
        heapq.heappush(left, -num)

        # 2. left 최대값 > right 최소값이면 교환
        #    즉, 중앙값 이하 집합(left)의 최댓값이 중앙값 초과 집합(right)의 최솟값보다 크면 잘못된 분배
        if right and -left[0] > right[0]:
            # left에서 최대값 꺼내서 right에 넣기
            val = -heapq.heappop(left)
            heapq.heappush(right, val)
            # right에서 최소값 꺼내서 left에 넣기
            val = heapq.heappop(right)
            heapq.heappush(left, -val)

        # 3. 두 힙의 크기 균형 맞추기
        #    left 크기는 항상 right보다 같거나 1 크게 유지
        if len(left) > len(right) + 1:
            val = -heapq.heappop(left)
            heapq.heappush(right, val)
        elif len(right) > len(left):
            val = heapq.heappop(right)
            heapq.heappush(left, -val)

        # 4. (i+1)번째 값이 홀수 번째 입력일 때 중앙값을 결과에 추가
        #    중앙값은 항상 left의 최대값(즉, -left[0])
        if (i + 1) % 2 == 1:
            res.append(-left[0])

    # 5. 출력
    # 첫 줄: 중앙값 개수
    print(len(res))
    # 중앙값들을 10개씩 끊어서 출력
    for i in range(0, len(res), 10):
        print(*res[i:i+10])
