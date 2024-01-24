from collections import deque
import sys
input = sys.stdin.readline


# e: 종료지점, n: 이동횟수
def move(e, n):
    ans = []

    temp = e
    for i in range(n):
        ans.append(temp)
        temp = v2[temp]

    print(*ans[::-1])


def bfs(s, e):
    global v2
    # 1. 큐, 방문 배열 선언
    q = deque()
    v = [0]*200001
    v2 = [0]*200001

    # 2. 초기값, 방문 배열 초기화
    q.append(s)
    v[s] = 1

    while q:
        c = q.popleft()
        # 수빈이 좌표 찾으면 종료 조건
        if c == e:
            print(v[e] - 1)
            move(c, v[e])
            return

        # 3방향 탐색
        for n in (c-1, c+1, c*2):
            if 0 <= n <= 200000 and v[n] == 0:
                q.append(n)
                v[n] = v[c] + 1
                v2[n] = c


n, k = map(int, input().split())    # 수빈이 위치, 동생 위치
bfs(n, k)