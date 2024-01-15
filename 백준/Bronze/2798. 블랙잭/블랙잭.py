from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

lst = list(map(int, input().split()))
Max = 0

for part in combinations(lst, 3):
    Sum = sum(part)
    if Sum <= M:
        Max = max(Max, Sum)
print(Max)