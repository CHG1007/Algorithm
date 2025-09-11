#   큐   실버 4

import sys
input = sys.stdin.readline

# 입력 처리
N = int(input())    # 명령의 수
q = []  # 큐

# 명령 처리
for _ in range(N):
    order = input().split()

    # push 연산
    if order[0] == "push":
        q.append(int(order[1]))
    # pop 연산
    elif order[0] == "pop":
        if q:
            print(q.pop(0))
        else:
            print(-1)
    # len 연산
    elif order[0] == "size":
        print(len(q))
    elif order[0] == "empty":
        if q:
            print(0)
        else:
            print(1)
    elif order[0] == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    elif order[0] == "back":
        if q:
            print(q[-1])
        else:
            print(-1)
    # print(order, q)
