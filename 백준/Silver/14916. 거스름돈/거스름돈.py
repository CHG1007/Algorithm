n = int(input())

ans = 0

if (n%5)%2 == 0:
    ans += n//5
    ans += (n%5)//2
else:
    if n < 4:
        ans = -1
    else:
        ans += n//5 - 1
        ans += ((n%5)+5)//2

print(ans)