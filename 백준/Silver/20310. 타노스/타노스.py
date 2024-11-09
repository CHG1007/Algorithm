s = list(input())
cnt_0, cnt_1 = 0, 0
for num in s:
    if num == '1':
        cnt_1 += 1
    else:
        cnt_0 += 1

cnt_0 = cnt_0//2
cnt_1 = cnt_1//2

ans = ''.join(s)

if cnt_1 >= 1:
    for i in range(len(s)):
        if s[i] == '1':
            s.remove('1')
            cnt_1 -= 1
        if cnt_1 == 0:
            break

s = s[::-1]
if cnt_0 >= 1:
    for i in range(len(s)):
        if s[i] == '0':
            s.remove('0')
            cnt_0 -= 1
        if cnt_0 == 0:
            break

s = s[::-1]
ans = ''.join(s)
print(ans)