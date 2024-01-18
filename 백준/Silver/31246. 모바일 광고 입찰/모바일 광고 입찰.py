import sys
input = sys.stdin.readline


N, K = map(int, input().split())
arr = []

for _ in range(N):
    A, B = map(int, input().split())
    arr.append(A-B)
arr.sort(reverse=True)

if arr[K-1] >= 0:
    print(0)
else:
    print((-1)*arr[K-1])