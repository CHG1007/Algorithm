import itertools

t = int(input())

for tc in range(t):
    n, l = map(int, input().split())

    lst = [list(map(int, input().split())) for _ in range(n)]
    ans = 0

    for i in range(1, n+1):
        # 재료를 1개부터 n개 까지 고르는 모든 경우의 수에 대해
        for data in itertools.combinations(lst, i):
            score, kal = 0, 0
            # 점수와 칼로리 누적 합산
            for value in data:
                kal += value[1]
                score += value[0]
                # 칼로리가 제한값을 넘지 않는다면
                if kal > l:
                    continue
                # 점수합산 최댓값 갱신
                if score > ans:
                    ans = score

    print(f'#{tc+1} {ans}')