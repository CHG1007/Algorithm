# 경로 찾기 실버 1

from collections import deque
import sys

input = sys.stdin.readline


# BFS 탐색
def bfs(s, N):
    # 1. 큐, 방문 배열 생성
    q = deque()
    v = [0]*(N+1)

    # 2. 초기 데이터 삽입, 방문 처리
    q.append(s)
    # v[s] = 1

    # 3. BFS 탐색

    while q:
        c = q.popleft()
        for n in graph[c]:
            if v[n] == 0:
                v[n] = 1
                q.append(n)

    return v


# 입력 처리
n = int(input())
graph = [[] for _ in range(n+1)]
ans = []

for i in range(1, n+1):
    tmp = list(map(int, input().split()))
    for j in range(len(tmp)):
        if tmp[j] == 1:
            graph[i].append(j+1)


for node in range(1, n+1):
    ans.append(bfs(node, n))

for line in ans:
    print(*line[1:])
