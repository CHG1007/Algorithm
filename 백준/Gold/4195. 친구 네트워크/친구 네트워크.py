#   친구 네트워크  골드 2

import sys
input = sys.stdin.readline


# 집합 초기화
def make():
    for i in range(2*F):
        parents[i] = i


# 집합의 대표자(부모) 반환 함수
def find(a):
    # 경로 압축
    while a != parents[a]:
        parents[a] = parents[parents[a]]
        a = parents[a]
    return a


# 서로소 집합이라면 합치는 함수
def union(a, b):
    a_root = find(a)
    b_root = find(b)

    # 집합의 대표자가 같다면 서로소 집합x -> 유니온 불가
    if a_root == b_root:
        return False
    # 집합의 대표자가 다르다면 서로소 집합o -> 유니온 가능
    else:
        # 트리의 크기에 따른 부모 트리 결정
        if size[b_root] > size[a_root]:
            a_root, b_root = b_root, a_root
        parents[b_root] = a_root        # 트리 합치기
        size[a_root] += size[b_root]    # 트리 크기 증가
        return True


# 입력 처리
T = int(input())    # 테스트 케이스 수
for _ in range(T):
    F = int(input())    # 친구 관계의 수

    parents = [0]*2*F   # 집합(트리) 초기화
    size = [1]*2*F      # 집합(트리)의 크기
    make()  # 집합 부모 초기화
    name = {}   # 사람 이름 딕셔너리
    N = 0       # 전체 사람 수
    ans = []    # 정답 리스트

    # F개의 친구 관계에 대해
    for i in range(F):
        A, B = input().split()    # 간선(친구) 정보
        if A not in name:
            name[A] = N
            N += 1
        if B not in name:
            name[B] = N
            N += 1
        # 간선 정보에 따른 연결(유니온 연산 실행)
        union(name[A], name[B])
        # 정답 누적
        ans.append(size[find(name[A])])

    # 정답 출력
    for num in ans:
        print(num)

