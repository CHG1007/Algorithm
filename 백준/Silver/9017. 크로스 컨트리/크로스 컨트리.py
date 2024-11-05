import sys
input = sys.stdin.readline


tc = int(input())

for _ in range(tc):
    rank = [0]*201
    team = []

    n = int(input())
    lst = list(map(int, input().split()))

    for num in lst:
        rank[num] += 1

    for i in range(len(rank)):
        if rank[i] == 6:
            team.append(i)

    score = [0]*n
    cnt = 1
    for i in range(n):
        if lst[i] in team:
            score[i] += cnt
            cnt += 1

    team_score = [0]*201
    team5 =[0]*201
    for t in team:
        cnt = 0
        for i in range(n):
            if lst[i] == t:
                team_score[t] += score[i]
                cnt += 1
            if cnt == 5:
                team_score[t] -= score[i]
                team5[t] += score[i]
                break

    min_score = max(team_score)
    for t in team:
        min_score = min(team_score[t], min_score)

    min5 = max(team5)
    for t in team:
        if team_score[t] == min_score:
            min5 = min(team5[t], min5)

    if team_score.count(min_score) == 1:
        print(team_score.index(min_score))
    else:
        print(team5.index(min5))