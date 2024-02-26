def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt
        
    for j in range(N):
        if k >= dungeons[j][0] and v[j] == 0:
            v[j] = 1
            dfs(k-dungeons[j][1], cnt+1, dungeons)
            v[j] = 0

def solution(k, dungeons):
    global answer, N, v
    N = len(dungeons)
    answer = 0
    v = [0]*N
    
    dfs(k, 0, dungeons)
    
    
    return answer