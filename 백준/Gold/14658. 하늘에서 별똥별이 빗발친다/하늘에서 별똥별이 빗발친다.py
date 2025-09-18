#   하늘에서 별똥별이 빗발친다  골드 3

import sys
input = sys.stdin.readline


# (si, sj)를 좌측 위 꼭지점으로 갖는 LxL 트럼팰린 내의 별똥별의 수 반환 함수
def cnt_star(si, sj):
    global ans
    cnt = 0
    # print("시작좌표: ", si, sj)

    # 트램펄린 좌상단을 필드 안으로 보정
    # 0<=si<=N-L, 0<=sj<=M-L
    # ⬇️ 축별로 '독립' 보정 (한 축이 L보다 짧아도 다른 축은 보정하지 않음)
    if N - L >= 0:
        si = max(0, min(si, N - L))
    if M - L >= 0:
        sj = max(0, min(sj, M - L))

    # 현재 트럼팰린 범위 안에 별똥별이 몇개 들어오는지 확인
    for star in stars:
        # 범위 내 -> 개수 추가 (경계 포함)
        if si<=star[0]<=si+L and sj<=star[1]<=sj+L:
            cnt += 1
        # x 정렬 기반 조기 종료
        if star[0] > si + L:
            break

    # 최대값 누적
    ans = max(cnt, ans)


# 입력
# N: 격자 가로 길이, M: 격자 세로 길이, L: 트럼팰린의 한 변의 길이, K: 별똥별의 수
N, M, L, K = map(int, input().split())
stars = []
ans = 0

for _ in range(K):
    # 별똥별의 위치 좌표
    x, y = map(int, input().split())
    stars.append((x, y))

# 별똥별 x, y 좌표 순으로 정렬
stars.sort(key=lambda x: (x[0], x[1]))

# 후보 좌표 (모든 별의 x, y좌표) + (별 좌표 - L) + (경계 0, N-L/M-L)
xs = set()
ys = set()

# 기본 별 좌표
for x, y in stars:
    xs.add(x)
    ys.add(y)
    # 우측/상단 경계에 별이 닿는 경우를 위해 좌하단을 (별.x-L, 별.y-L)로도 고려
    xs.add(x - L)
    ys.add(y - L)

# 경계 밀착 해도 후보에 포함
xs.add(0); ys.add(0)
xs.add(N - L); ys.add(M - L)

# 클램핑된 후보만 사용 (음수/범위초과 정리)
if N - L >= 0:
    xs = [max(0, min(v, N - L)) for v in xs]
else:
    xs = [0]  # 가로가 L보다 짧으면 x는 어디든 결과 동일 -> 0 하나만
if M - L >= 0:
    ys = [max(0, min(v, M - L)) for v in ys]
else:
    ys = [0]  # 세로가 L보다 짧으면 y는 어디든 결과 동일 -> 0 하나만

# 중복 제거 후 정렬(선택)
xs = sorted(set(xs))
ys = sorted(set(ys))

# 모든 후보 좌표에 대해 cnt_star 함수 실행
for si in xs:
    for sj in ys:
        cnt_star(si, sj)

# 정답 출력
print(K - ans)
