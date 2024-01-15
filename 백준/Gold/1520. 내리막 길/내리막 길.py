def dfs(ci,cj):
    if dp[ci][cj]==-1:                  # 아직 계산 안 된 경우(첫 방문)는 계산후 저장
        # 네 방향(더 높은곳으로부터 낮은곳방문시 경로수 누적
        dp[ci][cj]=0
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            pi,pj = ci+di, cj+dj        # 이전좌표 계산
            if arr[pi][pj]>arr[ci][cj]: # 내리막길인 경우
                dp[ci][cj]+=dfs(pi,pj)  # 조건에 맞는 네 방향 경로수 누적
    return dp[ci][cj]

N, M = map(int, input().split())
# 범위체크를 생략하기 위해서 0으로 둘러쌈
arr = [[0]*(M+2)]+[[0]+list(map(int, input().split()))+[0] for _ in range(N)]+[[0]*(M+2)]

# dp 테이블 생성 및 초기값 설정
dp = [[-1]*(M+2) for _ in range(N+2)]
dp[1][1] = 1

print(dfs(N,M))