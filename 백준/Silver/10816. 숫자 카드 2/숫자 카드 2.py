import sys
input = sys.stdin.readline


n = int(input())
nlst = list(map(int, input().split()))

m = int(input())
mlst = list(map(int, input().split()))

ans = [0]*20000001
for num in nlst:
    ans[num] += 1

for num in mlst:
    print(ans[num], end=' ')