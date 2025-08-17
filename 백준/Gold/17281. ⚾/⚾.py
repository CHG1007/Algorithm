import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
innings = [list(map(int, input().split())) for _ in range(N)]

max_score = 0

# 시뮬레이션 함수
def simulate(order):
    score = 0
    idx = 0  # 타자 인덱스 (0~8)

    for inning in innings:
        out_count = 0
        b1 = b2 = b3 = 0

        while out_count < 3:
            result = inning[order[idx]]

            if result == 0:
                out_count += 1
            elif result == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif result == 2:
                score += b3 + b2
                b1, b2, b3 = 0, 1, b1
            elif result == 3:
                score += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1
            elif result == 4:
                score += b1 + b2 + b3 + 1
                b1 = b2 = b3 = 0

            idx = (idx + 1) % 9

    return score


# 1번 선수(index 0)는 4번(index 3) 타자 고정
# 나머지 선수(1~8)로 순열 만들고 order 완성
for perm in permutations(range(1, 9)):
    order = [0] * 9
    order[3] = 0  # 4번 타자 고정
    idx = 0
    for i in range(9):
        if i == 3:
            continue
        order[i] = perm[idx]
        idx += 1

    max_score = max(max_score, simulate(order))

print(max_score)
