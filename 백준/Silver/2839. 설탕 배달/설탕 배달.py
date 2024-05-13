n = int(input())
ans = -1

for cnt_5 in range(n//5, -1, -1):
    cnt_3 = (n-cnt_5*5)//3
    if cnt_5*5 + cnt_3*3 == n:
        ans = cnt_3+cnt_5
        break

print(ans)