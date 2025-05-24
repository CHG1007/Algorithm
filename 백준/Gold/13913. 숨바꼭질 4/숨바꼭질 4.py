from collections import deque
import sys
input = sys.stdin.readline


def move(lst, target, cnt):
    ans = [target]  # 이동 경로 리스트(역순)
    tmp = target    # 경로 확인 변수
    
    # 이동 횟수 만큼 이동 경로 ans에 저장
    for _ in range(cnt):
        tmp = lst[tmp]
        ans.append(tmp)
    
    print(*ans[::-1])   # 역순 출력


def bfs(si, ei):
    # 1. 큐 생성, 방문 배열, 경로 배열 생성
    q = deque()
    v = [0]*(100001)
    path = [0]*(100001)

    # 2. 초기 데이터 삽입, 방문 처리
    q.append(si)
    v[si] = 1

    # 3. 3방향 탐색, 범위 10만, 방문 여부
    while q:
        ci = q.popleft()
        if ci == ei:
            print(v[ci]-1)
            move(path, ci, v[ci]-1)
            return

        for ni in ((ci-1), (ci+1), (2*ci)):
            if 0<=ni<=100000 and v[ni] == 0:
                q.append(ni)
                v[ni] = v[ci] + 1
                path[ni] = ci


n, k = map(int, input().split())
bfs(n, k)