from collections import deque
import sys
input = sys.stdin.readline

p = int(input())

for i in range(p):
    lst = deque(map(int, input().split()))
    tc = lst.popleft()
    cnt = 0
    q = []

    while True:
        student = lst.popleft()

        if q:
            if student > max(q):
                q.append(student)
            else:
                for j in range(len(q)):
                    if q[j] > student:
                        q = q[:j] + [student] + q[j:]
                        cnt += len(q) - (j+1)
                        break
        else:
            q.append(student)

        if len(q) == 20:
            break

    print(tc, cnt)