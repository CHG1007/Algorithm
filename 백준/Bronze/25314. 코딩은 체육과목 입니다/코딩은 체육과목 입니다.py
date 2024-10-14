n = int(input())
cnt = n//4
for _ in range(cnt):
    print('long ', end='')
if n != cnt*4:
    print('long ', end='')
print('int')