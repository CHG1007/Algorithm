#   스타트와 링크 실버 1


def power_team(team):
    power = 0
    for i in range(len(team)):
        for j in range(len(team)):
            if i != j:
                power += arr[team[i]][team[j]]

    return power


def dfs(idx, s_team):
    global ans
    if idx == n:
        if len(s_team) == n/2:
            l_team = list(set(lst)-set(s_team))
            ans = min(ans, abs(power_team(s_team)-power_team(l_team)))
        return

    dfs(idx+1, s_team+[idx+1])
    dfs(idx+1, s_team)


n = int(input())
arr = [[0]*(n+1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
lst = list(range(1, n+1))
ans = 10**9
dfs(0, [])
print(ans)


