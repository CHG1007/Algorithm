import sys
input = sys.stdin.readline


N, K = map(int, input().split())
arr = []

for _ in range(N):
    A, B = map(int, input().split())
    arr.append(A-B)
arr.sort(reverse=True)

print(max(0, -arr[K-1]))