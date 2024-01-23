N = int(input())

lst = list(map(int, input().split()))
lst2 = sorted(set(lst))

dic = {}
for i in range(len(lst2)):
    dic[lst2[i]] = i

for num in lst:
    print(dic[num], end=' ')