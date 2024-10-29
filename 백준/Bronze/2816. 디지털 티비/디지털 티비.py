n = int(input())
k1, k2 = 0, 0
ans = []
for i in range(n):
    ch = input()
    if ch == 'KBS1':
        k1 = i
    elif ch == 'KBS2':
        k2 = i


for i in range(k1):
    ans.append(1)
for i in range(k1):
    ans.append(4)

if k2<k1:
    for i in range(k2+1):
        ans.append(1)
    for i in range(k2):
        ans.append(4)
else:
    for i in range(k2):
        ans.append(1)
    for i in range(k2-1):
        ans.append(4)

result = ''
for s in ans:
    result += str(s)
print(result)