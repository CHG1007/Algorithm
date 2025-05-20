#   부분수열의 합 실버 2


def dfs(idx, total, cnt):
    global ans
    # 종료 조건(정답 처리)
    if idx == n:
        if total == s and cnt > 0:
            ans += 1
        return

    dfs(idx+1, total+lst[idx], cnt+1)   # 선택
    dfs(idx+1, total, cnt)              # 비선택


n, s = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0
dfs(0, 0, 0)
print(ans)
