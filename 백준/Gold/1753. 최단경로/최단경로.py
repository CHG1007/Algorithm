import sys, heapq
input = sys.stdin.readline

INF = 10**15  # 정수형 무한대

def dijkstra(start: int, graph: list[list[tuple[int,int]]]) -> list[int]:
    V = len(graph) - 1
    dist = [INF] * (V + 1)
    dist[start] = 0

    # 로컬 바인딩(미세 최적화)
    heappush = heapq.heappush
    heappop = heapq.heappop
    g = graph

    pq = []
    heappush(pq, (0, start))

    while pq:
        cur_d, u = heappop(pq)
        # 게으른 팝: PQ에서 나온 값이 최신 최단거리가 아니면 스킵
        if cur_d != dist[u]:
            continue
        for v, w in g[u]:
            nd = cur_d + w
            if nd < dist[v]:
                dist[v] = nd
                heappush(pq, (nd, v))
    return dist

# 입력
V, E = map(int, input().split())
K = int(input())

# 평행 간선 축약을 원하면 dict로 모은 뒤 리스트화 (선택)
# 여기선 속도/간단함을 위해 바로 리스트 사용
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))  # 방향 그래프(BOJ 1753 기준)

dist = dijkstra(K, graph)

# 빠른 출력
out = []
for i in range(1, V + 1):
    out.append("INF" if dist[i] == INF else str(dist[i]))
sys.stdout.write("\n".join(out))
