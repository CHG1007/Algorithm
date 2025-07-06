#   강아지는 많을수록 좋다    실버 1    개선버전
from collections import deque


def bfs(n, a, b, forbidden_ranges):
    queue = deque()
    visited = [0] * (n + 1)

    queue.append(0)
    visited[0] = 1

    while queue:
        cur = queue.popleft()

        # 목표 수에 도달했을 경우
        if cur == n:
            return visited[cur] - 1

        for d in (a, b):
            next_cnt = cur + d
            if 0 <= next_cnt <= n and visited[next_cnt] == 0:
                # 금지 구간에 포함되면 스킵
                for start, end in forbidden_ranges:
                    if start <= next_cnt <= end:
                        break
                else:
                    queue.append(next_cnt)
                    visited[next_cnt] = visited[cur] + 1

    # 도달 불가능
    return -1


# 입력 처리
n, m, a, b = map(int, input().split())
forbidden_ranges = [tuple(map(int, input().split())) for _ in range(m)]

# 결과 출력
print(bfs(n, a, b, forbidden_ranges))
