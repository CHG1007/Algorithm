import sys
input = sys.stdin.readline


def serch(target):
    start = 0
    end = N-1

    while start <= end:
        mid = (start+end)//2

        if nlst[mid] == target:
            return 1
        elif nlst[mid] > target:
            end = mid-1
        else:
            start = mid+1

    return 0


N = int(input())
nlst = sorted(list(map(int, input().split())))

M = int(input())
mlst = list(map(int, input().split()))

ans = []
for num in mlst:
    ans.append(serch(num))

print(*ans, sep='\n')