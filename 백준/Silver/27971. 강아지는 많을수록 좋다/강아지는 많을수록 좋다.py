from collections import deque


def bfs(end):
    q = deque()
    v = [0] * (n + 1)

    q.append(0)
    v[0] = 1

    while q:
        ci = q.popleft()
        if ci == end:
            return v[ci] - 1
        for di in (a, b):
            ni = ci + di
            if 0 <= ni <= n and v[ni] == 0:
                for l, r in lst:
                    if l <= ni <= r:
                        break
                else:
                    q.append(ni)
                    v[ni] = v[ci] + 1
    return -1


# 입력
n, m, a, b = map(int, input().split())
lst = [tuple(map(int, input().split())) for _ in range(m)]
print(bfs(n))
