def solution(sizes):
    # 가로, 세로 최대 높이
    w_max, h_max = 0, 0
    w_lst = []
    h_lst = []

    # 모든 명함의 가로, 세로에 대해
    for w, h in sizes:
        # 현재 명함의 가로, 세로중 큰 값을 저장후 w_max와 비교해 큰값 저장
        w_lst.append(max(w, h))

        # 현재 명함의 가로, 세로중 작은 값을 저장후 h_max 와 비교해 큰값 저장
        h_lst.append(min(w, h))

    # 가로 = 큰 값중 큰값 / 세로 = 작은값중 큰값
    answer = max(w_lst)*max(h_lst)

    return answer

