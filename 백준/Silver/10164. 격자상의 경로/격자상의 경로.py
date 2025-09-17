#   격자상의 경로     실버 2


#   - K가 0이면 (1,1)→(N,M) 경로 수
#   - K>0이면 (1,1)→K 경로 수 × K→(N,M) 경로 수
import sys
input = sys.stdin.readline


# K(1-based)를 (행, 열) 1-based 좌표로 변환
def k_to_rc(k, M):
    # k가 0이면 의미 없음
    if k == 0:
        return (-1, -1)
    r = (k - 1) // M + 1
    c = (k - 1) % M + 1
    return (r, c)


# 부분 격자 (sr,sc) → (er,ec) 로 "오른쪽/아래"만 이동하는 경로 수 DP
def count_paths(sr, sc, er, ec):
    # 범위가 역전되면 경로 없음
    if sr > er or sc > ec:
        return 0

    # 부분 격자 크기
    R = er - sr + 1
    C = ec - sc + 1

    # DP 테이블 생성
    dp = [[0]*C for _ in range(R)]

    # 시작 지점은 1
    dp[0][0] = 1

    # 첫 행 채우기: 왼쪽에서만 올 수 있음
    for j in range(1, C):
        dp[0][j] = dp[0][j-1]

    # 첫 열 채우기: 위에서만 올 수 있음
    for i in range(1, R):
        dp[i][0] = dp[i-1][0]

    # 나머지 채우기: 위/왼쪽 경로 수 합
    for i in range(1, R):
        for j in range(1, C):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    # print(*dp, sep='\n')
    # 정답 반환
    return dp[R-1][C-1]


# 입력 처리
N, M, K = map(int, input().split())

# 정답 출력
# K가 0이면 전체 한 번만 계산
if K == 0:
    ans = count_paths(1, 1, N, M)
    print(ans)
else:
    kr, kc = k_to_rc(K, M)          # K의 좌표(1-based)
    # 시작→K, K→끝 의 경로 수 곱
    left = count_paths(1, 1, kr, kc)
    right = count_paths(kr, kc, N, M)
    print(left * right)
