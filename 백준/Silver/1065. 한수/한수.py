N = int(input())

lst = list(range(1, 100))

for num in range(100, 1000):
    a = num//100
    b = num//10 - 10*a
    c = num%10
    if (b-a) == (c-b):
        lst.append(100*a+10*b+c)

ans = 0
for num in lst:
    if N >= num:
        ans += 1
    else:
        break

print(ans)