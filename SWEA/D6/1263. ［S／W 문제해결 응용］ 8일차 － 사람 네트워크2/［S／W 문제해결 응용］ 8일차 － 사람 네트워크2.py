# 1263. [S/W 문제해결 응용] 사람 네트워크2 (D6)

from collections import deque


# start 정점에서 시작해 BFS로 모든 최단거리를 구해 거리의 합을 반환하는 함수
# bound: 현재까지의 최소값(가지치기 용)
def bfs(start, bound):
    # 1. 큐 및 방문(최단거리) 배열 생성
    q = deque()
    dist = [-1] * N

    # 2. 초기값 대입
    q = deque([start])
    dist[start] = 0
    total = 0  # 최단거리 합(반환 값)

    # 3. BFS 탐색
    while q:
        cur_n = q.popleft()         # 현재 탐색 노드
        cur_n_dist = dist[cur_n]    # 현재 노드까지의 거리

        # 인접 노드 탐색
        for next in adj[cur_n]:
            if dist[next] == -1:  # 아직 방문하지 않은 경우
                dist[next] = cur_n_dist + 1  # 방문 처리 및 최단거리 갱신
                total += dist[next] # 합에 추가
                if total >= bound:  # 이미 최소값 초과 시 조기 종료
                    return total
                q.append(next)  # 다음 탐색 노드에 추가
    # 최단거리 합 반환
    return total


# 테스트 케이스 수 입력
T = int(input())
for tc in range(1, T + 1):
    data = list(map(int, input().split()))
    N = data[0]                 # 사람(노드) 수
    flat = data[1:]             # 사람 네트워크의 인접 행렬

    # 인접리스트 변환
    adj = [[] for _ in range(N)]  # 인접리스트 초기화
    idx = 0
    for i in range(N):
        for j in range(N):
            if flat[idx] == 1:    # i->j 연결 되었다면
                adj[i].append(j)  # 인접리스트에 추가
            idx += 1              # 인덱스 이동

    # 초기 최소값
    min_cc = 10**15

    # 모든 노드를 시작점으로 BFS 실행
    for start in range(N):
        cc_val = bfs(start, min_cc)
        # 최소값 갱신
        min_cc = min(min_cc, cc_val)

    # 정답 출력
    print(f"#{tc} {min_cc}")
