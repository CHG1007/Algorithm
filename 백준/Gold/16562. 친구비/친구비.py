#   친구비 골드 4

import sys
input = sys.stdin.readline


# 집합 초기화, 자신이 곧 자신의 부모
def make():
    for i in range(1, N+1):
        parents[i] = i


# 집합의 부모(대표자) 반환 함수
def find(a):
    while a != parents[a]:
        parents[a] = parents[parents[a]]
        a = parents[a]
    return a


# 서로소 집합이라면 합치는 함수
def union(a, b):
    a_root = find(a)
    b_root = find(b)

    if a_root == b_root:
        return False
    else:
        parents[b_root] = a_root
        return True


# 입력 처리
# N: 노드(학생) 수, M: 간선(친구관계) 수, k: 가지고 있는 돈
N, M, k = map(int, input().split())
cost = list(map(int, input().split()))  # 친구비
ans_cost = [[] for _ in range(N+1)]   # 대표자들 친구비

parents = [0]*(N+1)
# graph = [[] for _ in range(N+1)]    # 그래프 정보
Edge_lst = []   # 간선 정보
need_student = set()    # 집합의 대표 학생들

# 간선 정보 입력
for _ in range(M):
    v, w = map(int, input().split())
    # 무 방향 -> 양뱡 입력
    Edge_lst.append((v, w))
    # graph[v].append(w)
    # graph[w].append(v)

# 집합 초기화
make()

# 유니온 파인드 연산 실행
for (A, B) in Edge_lst:
    union(A, B)

for student in range(1, N+1):
    re_s = find(student)
    need_student.add(re_s)
    ans_cost[re_s].append(cost[student-1])

total = 0
for ns in need_student:
    tmp = 10**9
    for tmp_cost in ans_cost[ns]:
        tmp = min(tmp, tmp_cost)
    total += tmp

# 정답 출력
if k < total:
    print("Oh no")
else:
    print(total)

