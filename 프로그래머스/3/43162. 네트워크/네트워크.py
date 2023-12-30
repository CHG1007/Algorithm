

def bfs(s, v):
    # 큐와 방문배열 선언
    q = []

    # 큐에 초기 데이터 넣기
    q.append(s)
    v[s] = 1

    while q:
        c = q.pop(0)
        for n in adj[c]:
            if not v[n]:  # 방문하지 않았다면 큐에 삽입
                q.append(n)
                v[n] = 1


def solution(n, computers):
    global adj
    adj = [[] for _ in range(n+1)]
    v = [0] * (n+1)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                adj[i+1].append(j+1)

    print(adj)
    for i in range(1, n+1):
        if v[i] == 0:
            bfs(i, v)
            cnt += 1

    print(cnt)
    answer = cnt
    return answer

