

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


N, M = map(int, input().split())        # NxM 크기 방
r, c, direction = map(int, input().split())     # 시작좌표, 초기 방향
arr = [list(map(int, input().split())) for _ in range(N)]

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 방문 배열
v = [[0]*M for _ in range(N)]
v[r][c] = 1

count = 1       # 청소 횟수
turn_time = 0   # 회전 횟수

while True:
    # 왼쪽으로 회전
    turn_left()
    nx = r + dx[direction]
    ny = c + dy[direction]
    # 회전한 이후 정면에 방문하지 않은 칸이 있는 경우 이동
    if v[nx][ny] == 0 and arr[nx][ny] == 0:
        v[nx][ny] = 1
        r = nx
        c = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 벽인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = r - dx[direction]
        ny = c - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if arr[nx][ny] == 0:
            r = nx
            c = ny
        # 뒤가 벽으로 막혀있는 경우 작동 멈춤
        else:
            break
        turn_time = 0

# 정답 출력
print(count)