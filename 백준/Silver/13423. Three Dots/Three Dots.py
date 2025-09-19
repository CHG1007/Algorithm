#   Three Dots  실버 2


import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())    # 점의 개수
    A = list(map(int, input().split()))     # 점의 위치
    A.sort()    # 정렬
    S = set(A)  # 존재 여부 O(1) 확인용
    ans = 0

    # i < j만 순회 → 각 3쌍은 정확히 한 번만 카운트
    for j in range(N):
        aj = A[j]
        for i in range(j):
            ai = A[i]
            k = 2*aj - ai         # 등차수열의 세 번째 원소 후보(정수)
            if k in S:            # 존재하면 등차 3쌍 성립
                ans += 1
    # 정답 출력
    print(ans)
