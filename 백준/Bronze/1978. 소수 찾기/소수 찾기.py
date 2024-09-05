def prime(num):
    global ans
    cnt = 0
    for i in range(2, num+1):
        if num % i == 0:
            cnt += 1
        if cnt >= 2:
            return
    ans += 1


n = int(input())
lst = list(map(int, input().split()))
ans = 0

for num in lst:
    if num == 1:
        continue
    prime(num)

print(ans)