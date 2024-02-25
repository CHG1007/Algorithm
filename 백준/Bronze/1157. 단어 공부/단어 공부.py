word = input()

lst = [0]*26

for s in word:
    tmp = ord(s)
    if tmp >= 97:
        tmp -= 32
    lst[tmp-65] += 1

cnt = 0
ans = 0
for i in range(len(lst)):
    if lst[i] == max(lst):
        ans = i
        cnt += 1
    if cnt > 1:
        break

if cnt > 1:
    print('?')
else:
    print(chr(65+ans))