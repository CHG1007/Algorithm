#   파핑파핑 지뢰찾기 D4    4:05

# 표에서 지뢰가 0인칸 클릭 및 방문 하기
def zero(si, sj):
    # 8방향 탐색
    ci, cj = si, sj

    for di, dj in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
        ni, nj = ci+di, cj+dj
        # 표 범위조건, 지뢰 여부, 방문 여부 확인
        if 0 <=ni<n and 0<=nj<n and arr[ni][nj] != '*' and not v[ni][nj]:
            # 방문처리
            v[ni][nj] = True
            # 만약 8방향중 값이 0 이라면 새로운 8방향 좌표 탐색
            if arr[ni][nj] == 0:
                zero(ni, nj)


# 8방향 지뢰 갯수 반환 함수
def check(si, sj):
    ci, cj = si, sj
    cnt = 0     # 지뢰 갯수

    for di, dj in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
        ni, nj = ci+di, cj+dj
        # 표 범위조건, 지뢰 인지 확인
        if 0<=ni<n and 0<=nj<n and arr[ni][nj] == '*':
            cnt += 1
    return cnt


t = int(input())

for tc in range(t):
    n = int(input())
    arr = [list(input()) for _ in range(n)]     # 표

    v = [[False]*n for _ in range(n)]   # 방문 배열
    ans = 0     # 최소 클릭 수

    # 표에서 지뢰가 아닌칸에 지뢰 개수 채우기
    for i in range(n):
        for j in range(n):
            # 지뢰가 없는 칸이라면
            if arr[i][j] == '.':
                arr[i][j] = check(i, j)

    # 표에서 지뢰가 0인칸 중 방문하지 않았다면 클릭
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0 and not v[i][j]:
                v[i][j] = True
                zero(i, j)
                ans += 1

    # 지뢰가 아닌칸인데 방문 하지 않았다면 칸 갯수만큼 클릭수 누적
    for i in range(n):
        for j in range(n):
            if arr[i][j] != '*' and not v[i][j]:
                ans += 1

    print(f'#{tc+1} {ans}')
