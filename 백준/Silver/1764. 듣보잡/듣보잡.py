#   듣보잡 실버 4

import sys
input = sys.stdin.readline

# 입력 처리
n, m = map(int, input().split())

# set 사용
heard = set(input().strip() for _ in range(n))
seen = set(input().strip() for _ in range(n))

# 교집합
ans = sorted(heard & seen)

# 출력
print(len(ans), *ans, sep='\n')
