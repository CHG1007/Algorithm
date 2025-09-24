#   알고리즘 수업 - 너비 우선 탐색 2    실버 2

from collections import deque
import sys
input = sys.stdin.readline

# bfs 탐색 함수
# graph: 인접 그래프, v: 방문 배열, s: 시작 정점
def bfs(graph, v, s):
    # 1. 큐, 방문 순서 변수 생성
    q = deque()
    order = 1

    # 2. 초기값 입력
    q.append(s)
    v[s] = order

    # 3. bfs 탐색
    while q:
        cur_node = q.popleft()  # 현재 정점
        for nxt_node in graph[cur_node]:    # 현재 정점과 인접한 모든 정점들에 대해서
            if v[nxt_node] == 0:    # 미방문 이라면
                order += 1      # 방문 순서 늘린후
                v[nxt_node] = order     # 방문 처리
                q.append(nxt_node)      # 다음 탐색 정점에 추가


# 입력 처리
N, M, R = map(int, input().split())     # N: 정점의 수, M: 간선의 수, R: 시작 정점

graph = [[] for _ in range(N+1)]    # 인접 그래프

for _ in range(M):
    # U->V 간선 존재(무방향)
    U, V = map(int, input().split())
    # 양방향 입력
    graph[U].append(V)
    graph[V].append(U)

# 정점 번호 내림차순 정렬
for node in graph:
    node.sort(reverse=True)

v = [0]*(N+1)   # 방문 배열

# bfs 함수 호출
bfs(graph, v, R)

# 정답 출력
print(*v[1:], sep='\n')
