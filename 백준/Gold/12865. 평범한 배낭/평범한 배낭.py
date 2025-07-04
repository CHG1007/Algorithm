#   평범한 배낭  골드 5


# 입력 처리
n, k = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(n)]

# dp[i]: 무게가 i일때 얻을 수 있는 '최대 가치'
dp = [0]*(k+1)

# 각 물건을 하나씩 처리
for w, v in items:
    # 현재 물건의 무게가 w, 가치가 v인 경우
    # 현재 물건을 넣을 수 있는 배낭 무게부터 역순으로 순회
    for i in range(k, w-1, -1):
        # i: 현재 배낭의 무게 한계
        # dp[i]: 기존 이 무게에서 도달 가능한 최대 가치
        # dp[i-w] + v: 이 물건을 추가했을 때의 총 가치
        dp[i] = max(dp[i], dp[i-w]+v)

print(dp[k])

