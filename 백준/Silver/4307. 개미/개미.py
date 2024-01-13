import sys

input = sys.stdin.readline


def dis(q):
    q2 = []
    short = 0
    for c in q:
        short = max(short, min(L-c, c))

    print(short, max(L-q[0], q[-1]))


T = int(input())

for _ in range(T):
    q = []
    L, N = map(int, input().split())

    for _ in range(N):
        q.append(int(input()))

    q.sort()
    dis(q)