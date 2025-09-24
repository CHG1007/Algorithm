#   알고리즘 수업 - 너비 우선 탐색 1    실버 2

from collections import deque
import sys
input = sys.stdin.readline

# bfs 탐색 함수
# graph: 인접 그래프, v: 방문 배열, s: 시작 정점
def bfs(graph, v, s):
    # 1. 큐 생성, 거리 변수 생성
    q = deque()
    dist = 1

    # 2. 초기값 대입
    q.append(s)
    v[s] = dist

    # 3. bfs 탐색
    while q:
        cur_node = q.popleft()  # 현재 노드
        for next_node in graph[cur_node]:   # 현재 노드와 인접한 모든 노드들에 대해
            if v[next_node] == 0:           # 미방문 이라면
                dist += 1   # 거리 계산 후
                v[next_node] = dist     # 방문 처리
                q.append(next_node)     # 다음 탐색 노드에 추가


# 입력 처리
N, M, R = map(int, input().split())     # N: 정점의 수, M: 간선의 수, R: 시작 정점

graph = [[] for _ in range(N+1)]    # 인접 그래프
Edge_lst = []   # 간선 정보
v = [0]*(N+1)   # 방문 배열

for _ in range(M):
    # u->v 간선 존재
    U, V = map(int, input().split())
    Edge_lst.append((U, V))
    Edge_lst.append((V, U))

# 정점 번호 순 정렬
Edge_lst.sort(key=lambda x: (x[0], x[1]))

# 간선 정보 그래프에 입력
for (s, e) in Edge_lst:
    graph[s].append(e)

# bfs 실행
bfs(graph, v, R)
# 정답 출력
print(*v[1:], sep='\n')
