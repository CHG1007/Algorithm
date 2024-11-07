import sys
input = sys.stdin.readline

n, x = map(int, input().split())
lst = list(map(int, input().split()))

# x일 동안 방문자 합
total = sum(lst[:x])
# 최대 방문자, 최대 방문자 기간 수
max_visit, cnt = total, 1

for i in range(1, n-(x-1)):
    # i일 기준 x일 동안 방문자 합
    total += lst[i+(x-1)] - lst[i-1]
    
    if total == max_visit:      # 직전 최대 방문자 합과 같다면
        cnt += 1                # 기간 수 증가
    elif total > max_visit:     # 합이 더 크다면
        max_visit = max(max_visit, total)   # 최대값 갱신
        cnt = 1                 # 기간 수 초기화

if max_visit == 0:
    print('SAD')
else:
    print(max_visit)
    print(cnt)
