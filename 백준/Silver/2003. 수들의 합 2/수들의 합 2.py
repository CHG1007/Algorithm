#   수들의 합 2 실버 4    개선 버전


# 입력 처리
n, m = map(int, input().split())
lst = list(map(int, input().split()))

left = 0
right = 0
current_sum = 0
ans = 0

while True:
    # 누적합이 목표 미만이면, 우측값 더하고, 우측 포인터 한칸 증가
    if current_sum < m:
        if right == n:
            break
        current_sum += lst[right]
        right += 1
    # 누접합이 목표 이상이면, 정답체크, 왼쪽 값을 빼고, 왼쪽 포인터 한칸 증가
    else:
        if current_sum == m:
            ans += 1
        current_sum -= lst[left]
        left += 1

print(ans)
