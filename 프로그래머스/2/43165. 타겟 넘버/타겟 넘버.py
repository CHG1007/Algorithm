from collections import deque


def bfs(lst, target):
    # 1. 큐 생성
    q = deque()
    n_q = deque()

    # 2. 초기 데이터
    s_n = lst.popleft()
    q.append(-s_n)
    q.append(s_n)
    cnt = 0

    # 3. 탐색
    while lst:
        next_n = lst.popleft()
        while q:
            c_n = q.popleft()
            for choice in (-next_n, next_n):
                n_q.append(c_n+choice)
        while n_q:
            q.append(n_q.popleft())

    for num in q:
        if num == target:
            cnt += 1

    return cnt


def solution(numbers, target):
    numbers = deque(numbers)
    answer = bfs(numbers, target)

    return answer