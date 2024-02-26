def dfs(k, cnt, dungeons):
    global ans
    if cnt > ans:
        ans = cnt
    
    for j in range(N):
        if k >= dungeons[j][0] and v[j] == 0:
            v[j] = 1
            dfs(k-dungeons[j][1], cnt+1, dungeons)
            v[j] = 0

def solution(k, dungeons):
    global N, v, ans
    N = len(dungeons)
    ans = 0
    v = [0]*N
    
    dfs(k, 0, dungeons)
    
    return ans