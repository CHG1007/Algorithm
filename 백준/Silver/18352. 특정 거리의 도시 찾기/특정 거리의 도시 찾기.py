from collections import deque
import sys
input = sys.stdin.readline

def bfs(start_city):
    q = deque()
    v = [-1] * (n + 1)  # -1로 초기화: 방문 여부 + 거리 정보
    v[start_city] = 0   # 시작 도시는 거리 0

    q.append(start_city)

    while q:
        current_city = q.popleft()

        for next_city in graph[current_city]:
            if v[next_city] == -1:
                v[next_city] = v[current_city] + 1
                q.append(next_city)

    return v

# 입력 처리
n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)

result_distance = bfs(x)

ans = []
for city, distance in enumerate(result_distance):
    if distance == k:
        ans.append(city)

if not ans:
    print(-1)
else:
    ans.sort()
    print(*ans, sep='\n')
