from collections import deque


def bfs(lost, reserve):
    # 1. 큐(여분의 체육복이 있는 학생 리스트) , lost 방문 배열
    q = deque(reserve)
    v = [0]*31

    # 2. 초기데이터, 체육복을 빌려준 횟수
    cnt = 0

    # 3. 탐색
    while q:
        c = q.popleft()

        # 2방향, 방문 조건(이미 빌려준 학생인지 여부)
        for nc in c - 1, c + 1:
            if nc in lost:          # reserve 번호의 앞, 뒤 번호에 lost 번호가 있고
                if v[nc] == 0:      # 해당 lost 번호에 방문하지(빌려주지) 않았다면
                    v[nc] += 1      # 해당 lost 번호에 방문처리후 빌려주기
                    cnt += 1        # 체육복을 빌려준 횟수 카운트
                    break           # 앞에 빌려줬으면 즉시 종료

    return cnt


def solution(n, lost, reserve):
    # 중복 제거
    for data in lost[:]:
        if data in reserve:
            reserve.remove(data)
            lost.remove(data)

    # 정렬
    lost.sort()
    reserve.sort()

    # 총 학생수 - 현재 체육복이 없는 학생 수 + 빌릴 수 있는 경우의 수
    answer = n - len(lost) + bfs(lost, reserve)

    return answer
