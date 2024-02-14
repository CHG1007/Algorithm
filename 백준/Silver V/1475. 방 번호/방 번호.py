import math

N = list(input())
lst = [0]*11

for num in N:
    lst[int(num)] += 1

card = lst[6]+lst[9]
lst[6], lst[9] = 0, 0

ans = max(max(lst), math.ceil(card/2))
print(ans)