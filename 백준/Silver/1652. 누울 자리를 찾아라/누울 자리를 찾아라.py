def cnt(Map):
    ans = 0
    for line in Map:
        s = ''.join(line)
        for slice in s.split('X'):
            if len(slice) >= 2:
                ans += 1
    return ans


n = int(input())

arr = [list(input()) for _ in range(n)]

print(cnt(arr), cnt(list(zip(*arr))))