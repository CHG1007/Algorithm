#   나무 자르기 실버 2

import sys
input = sys.stdin.readline


# 높이 설정을 mid로 했을때 가져가는 나무가 M미터 이상 가능한지 반환하는 함수
def check(mid):
    total = 0   # 총 가져가는 나무의 양
    for cur_tree in tree:
        need = cur_tree - mid   # 각 나무마다 가져가는 양
        if need > 0:
            total += need
            # 가지치기 (이미 필요량 채웠다면)
            if total >= M:
                return True
    # 가져가는 나무의 합이 M이상 이라면 True / 아니면 False 반환
    return total >= M


# 입력 처리
N, M = map(int, input().split())    # N: 나무의 수, M: 가져갈 나무의 길이
tree = list(map(int, input().split()))  # 나무 높이

max_tree = max(tree)    # 최대 나무 높이

# 이분 탐색위한 변수
lo = 0  # 하한값
hi = max_tree+1     # 상한값

# 이분탐색 -> io와 hi 사이에는 최소한 1개의 값이 존재하도록 설계
while lo+1 < hi:
    mid = (lo + hi) // 2

    # mid 높이로 잘랐을때 -> M미터 이상 나무를 가져 갈 수 있다면 -> 자르는 높이 최대한 높이기
    if check(mid):
        lo = mid
    # mid 높이로 잘랐을때 -> M미터 이상 나무를 가져 갈 수 없다면 -> 자르는 높이 낮추기
    else:
        hi = mid

# 정답 출력
print(lo)
