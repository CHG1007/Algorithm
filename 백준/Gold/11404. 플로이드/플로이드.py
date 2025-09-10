#   플로이드    골드 4

import sys
input = sys.stdin.readline


INF = 1e9
# INF = 100

# 입력 처리
N = int(input())    # 도시의 개수
M = int(input())    # 버스의 개수

# 인접 행렬(거리 테이블) 생성 및 초기화
# dist[i][j]: i->j 최소 비용. 초기에는 INF, 자기 자신은 0
dist = [[INF]*(N) for _ in range(N)]
for i in range(N):
    # 자기 자신은 0
    dist[i][i] = 0

# print()
# print(*dist, sep='\n')
# print('-'*10)

# 간선 입력(초기값 입력)
# 같은(a, b) 쌍에 대해 여러 간선이 있을 수 있으므로, 더 작은 비용만 반영
for _ in range(M):
    a, b, c = map(int, input().split())
    # 현재 a->b 비용보다 작은 비용이라면 반영
    if c < dist[a-1][b-1]:
        dist[a-1][b-1] = c


# 플로이드 워셜
for k in range(N):     # 경유지
    for i in range(N):     # 출발지
        for j in range(N):     # 도착지
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

# 불가능 경로 -> 0            
for i in range(N):
    for j in range(N):
        if dist[i][j] == INF:
            dist[i][j] = 0

# 정답 출력
for line in dist:
    print(*line)





