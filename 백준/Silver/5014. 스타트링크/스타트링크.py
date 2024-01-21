from collections import deque
import sys
input = sys.stdin.readline


def bfs(si, ei):
    # 1. 큐, 방문배열 생성
    q = deque()
    v = [0] * (F + 1)

    # 2. 초기 데이터 입력
    q.append(si)
    v[si] = 1

    # 3. 탐색
    while q:
        ci = q.popleft()
        if ci == ei:
            return v[ci]-1

        for ni in ((ci - D), (ci + U)):
            if 1 <= ni <= F and v[ni] == 0:
                v[ni] = v[ci] + 1
                q.append(ni)

    return 'use the stairs'


F, S, G, U, D = map(int, input().split())

print(bfs(S, G))