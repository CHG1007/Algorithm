import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# set 사용
heard = set(input().strip() for _ in range(n))
seen = set(input().strip() for _ in range(m))

# 교집합
result = sorted(heard & seen)

# 출력
print(len(result))
print("\n".join(result))
