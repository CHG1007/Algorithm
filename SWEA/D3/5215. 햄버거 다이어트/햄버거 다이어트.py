import itertools


t = int(input())
for tc in range(t):
    n, l = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]

    max_score = 0

    for i in range(1, n+1):
        for value in itertools.combinations(data, i):
            kcal = 0
            score = 0
            for v in range(len(value)):
                kcal += value[v][1]
                score += value[v][0]
            if kcal > l:
                continue
            if max_score < score:
                max_score = score

    print(f'#{tc+1} {max_score}')