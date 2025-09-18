#   차이를 최대로 실버 2

import itertools

# 입력 처리
N = int(input())    # 정수의 개수
lst = list(map(int, input().split()))   # 입력 배열
ans = 0

# 완탐으로 풀어보자
# lst 숫자 배열을 순서를 구분해 N개 뽑는 모든 경우의 수에 대해서
for permu in itertools.permutations(lst, N):
    tmp = 0
    # 배열의 값 계산
    for i in range(len(permu) - 1):
        tmp += abs(permu[i] - permu[i + 1])
    # 정답 갱신
    ans = max(tmp, ans)

# 정답 출력
print(ans)

