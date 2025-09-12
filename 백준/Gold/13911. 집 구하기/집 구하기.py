#   집 구하기   골드 2

import heapq
import sys
input = sys.stdin.readline

INF = 10**14


# 시작점이 여러개인(starts 배열) 다익스트라 -> 최단 거리 테이블 반환
def dijkstra_multi(starts, graph, V):
    # 1. 큐 생성, 최단 거리 테이블 생성
    q = []
    distance = [INF]*(V+1)

    # 2. 초기값 입력
    for s in starts:
        distance[s] = 0
        # (현재까지의 거리, 정점) 형태로 입력
        heapq.heappush(q, (0, s))

    # 3. 탐색
    while q:
        # 현재 가장 거리가 짧은 노드 정보 꺼내기
        # dist: now노드 까지의 거리, cn: 현재 노드
        dist, cn = heapq.heappop(q)

        # 현재 노드가 이미 처리된 적이 있다면 무시
        if distance[cn] < dist:
            continue
        # 현재 노드와 인접한 다른 노드들을 확인
        for (nn, ndist) in graph[cn]:
            # 현재 노드까지의 거리와 다음 노드 까지의 거리의 합
            cost = dist + ndist
            # 현재 노드를 거쳐서 다음 노드로 가는 거리가 더 짧다면
            if cost < distance[nn]:
                # 거리 테이블 갱신
                distance[nn] = cost
                # 다음 탐색 노드 추가
                heapq.heappush(q, (cost, nn))

    # 최단거리 배열 반환
    return distance


# 입력 처리
V, E = map(int, input().split())    # V: 정점의 개수, E: 도로의 개수
graph = [[] for _ in range(V+1)]    # 그래프


# 그래프 정보 입력
for _ in range(E):
    # u->v 비용 w 도로
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

# 맥도날드 정보
M, limit_m = map(int, input().split())
lst_m = set(map(int, input().split()))

# 스타벅스 정보
S, limit_s = map(int, input().split())
lst_s = set(map(int, input().split()))

# 멀티 소스 다익스트라 2회 실행
distM = dijkstra_multi(lst_m, graph, V)
distS = dijkstra_multi(lst_s, graph, V)

# 정답 변수
ans = INF

# 모든 집 정점에 대해서 거리 조회
for h in range(1, V + 1):
    if h in lst_s or h in lst_m:
        continue
    # 각각 맥세권과 스세권 거리를 만족하면 정답 갱신
    if distM[h] <= limit_m and distS[h] <= limit_s:
        ans = min(ans, distM[h] + distS[h])


# 정답 출력
print(-1 if ans == INF else ans)


