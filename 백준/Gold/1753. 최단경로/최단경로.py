#   최단경로    골드 4

import heapq
import sys
input = sys.stdin.readline


# 다익스트라
def dijkstra(start):
    # 1. 큐 생성
    q = []

    # 2. 초기값 입력
    heapq.heappush(q, (0, start))   # q에 (현재 노드까지의 거리, 현재 노드) 삽입
    distance[start] = 0     # 현재 노드 까지의 거리는 0 설정

    # 3. 탐색
    while q:
        # 현재 가장 거리가 짧은 노드에 대한 정보 꺼내기
        cur_dist, cur_node = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면(이미 최단거리가 더 짧다면) 무시
        if distance[cur_node] < cur_dist:
            continue
        # 현재 노드와 인접한 다른 노드들을 확인
        for (next_node, next_dist) in graph[cur_node]:
            # 현재 노드까지의 최소 비용과 다음 노드 까지의 비용의 합
            cost = cur_dist + next_dist
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧다면
            if cost < distance[next_node]:
                # 거리 테이블 갱신
                distance[next_node] = cost
                # 다음 탐색 노드로 추가
                heapq.heappush(q, (cost, next_node))


# 입력 처리
V, E = map(int, input().split())    # V: 정점의 개수, E: 간선의 개수
K = int(input())    # 시작 정점의 번호
graph = [[] for _ in range(V+1)]    # 그래프 정보
distance = [1e9]*(V+1)  # 최단거리 테이블

# 간선 정보 입력 받기
for _ in range(E):
    # u->v 비용 w
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# 다익스트라 실행 -> 시작 노드 K 파라미터 전달
dijkstra(K)

# 정답 출력
for i in range(1, V+1):
    if distance[i] == 1e9:
        print("INF")
    else:
        print(distance[i])


