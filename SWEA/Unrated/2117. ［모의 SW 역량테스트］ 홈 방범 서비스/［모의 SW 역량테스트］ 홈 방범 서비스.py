#   2117. [모의 SW 역량테스트] 홈 방범 서비스


# 중심 좌표가 (si, sj)이고 운영 영역의 크기가 2*K-1 일때
# 손해를 보지 않으면서 서비스를 제공하는 집의 수를 반환하는 함수
def cal(si, sj, K):
    radius = K-1    # 마름모 반경
    cnt_home = 0    # 서비스 영역의 집 갯수
    cost = K**2+(K-1)**2  # K 서비스 영역의 비용

    # 마름모 영역 탐색
    # 마름모가 격자 밖으로 나가지 않도록 행 인덱스 조절
    row_start = max(0, si-radius)     # 시작 행: 중심에서 위로 radius
    row_end = min(N-1, si+radius)     # 마지막 행: 중심에서 아래로 radius

    for row in range(row_start, row_end + 1):
        # 중심에서 좌우로 퍼질 수 있는 거리
        offset = radius-abs(row-si)

        # 마름모가 격자 밖으로 나가지 않도록 열 인덱스 조절
        col_start = max(0, sj-offset)
        col_end = min(N-1, sj+offset)

        # 유효 범위 내 집 범위 카운트
        for col in range(col_start, col_end + 1):
            if arr[row][col] == 1:
                cnt_home += 1

    # 손해를 보지 않았다면 해당 영역의 집 갯수 반환
    return cnt_home if cnt_home*M - cost >= 0 else 0


# 입력 처리
T = int(input())    # 테스트 케이스 수
for tc in range(T):
    # N: 도시의 크기, M: 하나의 집이 지불할 수 있는 비용
    N, M = map(int, input().split())
    # NxN 도시정보
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 정답 변수
    ans = 0

    # 영역 K를 증가시키며 모든 좌표를 중심으로 cal 계산 및 정답 갱신(최대값)
    for K in range(1, N+2):
        for i in range(N):
            for j in range(N):
                ans = max(cal(i, j, K), ans)

    # 정답 출력
    print(f'#{tc+1} {ans}')




