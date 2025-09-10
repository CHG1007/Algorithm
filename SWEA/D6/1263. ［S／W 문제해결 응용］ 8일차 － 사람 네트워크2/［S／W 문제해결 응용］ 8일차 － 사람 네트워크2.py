#   1263. [S/W 문제해결 응용] 8일차 - 사람 네트워크2 D6

from collections import deque


# 입력 처리
T = int(input())    # 테스트 케이스 수
for tc in range(1, T + 1):
    lst = list(map(int, input().split()))
    N = lst[0]  # 사람(노드) 수
    flat = lst[1:]  # 사람 네트워크 인접 행렬

    need = N * N

    # 인접리스트로 변환
    adj = [[] for _ in range(N)]

    idx = 0
    for i in range(N):
        # 행을 슬라이스로 꺼내면 O(N) 복사가 생기므로 인덱스로 접근
        for j in range(N):
            if flat[idx] == 1:
                # 무방향 그래프
                adj[i].append(j)
            idx += 1

    # 3) BFS 함수: 시작노드 s에서 모든 정점까지 최단거리 합을 계산
    def cc_sum_from(s, best_so_far):
        # dist[v] = s로부터 v까지의 최단거리, 미방문은 -1
        dist = [-1] * N
        dist[s] = 0

        q = deque([s])
        reached = 1         # 도달한 정점 수 (연결성 검증용)
        total = 0           # 최단거리 합 Σ dist(s, v)

        while q:
            u = q.popleft()
            du = dist[u]
            # u의 모든 이웃을 탐색
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = du + 1
                    total += dist[v]
                    reached += 1
                    # 프루닝: 현재 최소값을 이미 넘으면 더 볼 필요 없음
                    if best_so_far is not None and total >= best_so_far:
                        return total
                    q.append(v)

        return total

    # 4) 모든 시작점에 대해 BFS, 최소 CC 값 갱신
    answer = 10**15
    for s in range(N):
        cur = cc_sum_from(s, answer)   # 현재 최소값을 넘으면 내부에서 조기 종료
        if cur < answer:
            answer = cur
    # 정답 출력
    print(f"#{tc} {answer}")
