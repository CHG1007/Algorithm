# SWEA 5653. [모의 SW 역량테스트] 줄기세포배양

# 키가 없을 때 자동으로 기본값(list)을 생성
from collections import defaultdict


def simulate(initial_cells, K):
    # 모든 점유 칸 관리 (죽은 세포도 점유 상태 유지)
    # key: (r, c), value: (life, created_time)
    cells = {}

    # 번식 이벤트 테이블: repro[t] = [(life, ct, r, c), ...]
    repro = defaultdict(list)

    # 초기 세포 등록(생성 시각 = 0) 및 첫 번식 스케줄링
    for r, c, life in initial_cells:
        cells[(r, c)] = (life, 0)   # 초기 배양판에서 세포가 있는 좌표만 반복
        t = life + 1                # 0 + life + 1
        if t <= K:
            repro[t].append((life, 0, r, c))

    # 4방향(상, 하, 좌, 우)
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 시간 1 ~ K: 번식 이벤트만 처리하는 시뮬레이션
    for t in range(1, K + 1):
        if t not in repro:
            continue

        # 이번 시각에 생성될 후보: 같은 칸 겹치면 life 큰 쪽이 이김
        proposals = {}  # (nr, nc) -> best_life
        for life, ct, r, c in repro[t]:
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                # 이미 점유된 칸(죽은 세포 포함)이면 불가
                if (nr, nc) in cells:
                    continue
                # 좌표별 최대 생명력 유지
                if (nr, nc) not in proposals or proposals[(nr, nc)] < life:
                    proposals[(nr, nc)] = life

        # 후보를 실제 생성으로 확정하고, 다음 번식도 스케줄링
        for (nr, nc), life in proposals.items():
            cells[(nr, nc)] = (life, t)           # 생성
            nt = t + life + 1                     # 다음 번식 시각
            if nt <= K:
                repro[nt].append((life, t, nr, nc))

    # K시간 후 살아있는 세포 수(비활성+활성) 계산
    alive = 0
    for life, ct in cells.values():
        # 죽는 시각 = ct + 2*life, 그 이전이면 살아있음
        if ct + 2 * life > K:
            alive += 1
    return alive


# 입력처리
T = int(input().strip())
for tc in range(1, T + 1):
    # N: 세로 크기, M: 가로 크기, K: 배양 시간
    N, M, K = map(int, input().split())
    # 초기 세포 정보 리스트
    initial = []
    for r in range(N):
        row = list(map(int, input().split()))
        for c, x in enumerate(row):
            if x > 0:
                initial.append((r, c, x))

    # print(*initial, sep='\n')

    # K시간 후 살아있는 세포(비활성+활성)의 총 개수
    ans = simulate(initial, K)
    print(f"#{tc} {ans}")
