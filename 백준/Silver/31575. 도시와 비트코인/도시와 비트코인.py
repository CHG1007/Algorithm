#   도시와 비트코인    실버 3

from collections import deque
import sys
input = sys.stdin.readline


# bfs 함수
def bfs(si, sj):
    # 1. 큐, 방문 배열, 도착 위치 변수 생성
    q = deque()
    v = [[0]*N for _ in range(M)]
    ei, ej = M-1, N-1

    # 2. 초기값 입력
    q.append((si, sj))
    v[si][sj] = 1

    # 3. 2방향(오른쪽, 아래쪽) 탐색
    while q:
        ci, cj = q.popleft()    # 현재 좌표
        # 남동쪽 끝에 도달 가능하면 즉시 종료("Yes" 반환)
        if (ci, cj) == (ei, ej):
            return "Yes"
        # 2방향
        for di, dj in ((0, 1), (1, 0)):
            ni, nj = ci+di, cj+dj
            # 도시 격자 범위, 방문 여부, 맵 조건 확인
            if 0<=ni<M and 0<=nj<N and v[ni][nj] == 0 and arr[ni][nj] == 1:
                v[ni][nj] = 1   # 방문처리
                q.append((ni, nj))  # 다음 탐색 좌표 추가
    # 도달 불가시 종료("No" 반환)
    return "No"


# 입력 처리
N, M = map(int, input().split())    # N: 도시의 가로, M: 도시의 세로
arr = [list(map(int, input().split())) for _ in range(M)]   # 도시

# bfs 함수 실행
ans = bfs(0, 0)

# 정답 출력
print(ans)


