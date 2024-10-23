import sys
from operator import itemgetter, attrgetter
input = sys.stdin.readline


n, k = map(int, input().split())
arr = []*n
ans = 0
for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=itemgetter(1,2,3), reverse=True)

for i in range(len(arr)):
    if arr[i][0] == k:
        ans = i+1
        for j in range(i, 0, -1):
            if arr[j][1:] == arr[j-1][1:]:
                ans -= 1
            else:
                break
        break
print(ans)