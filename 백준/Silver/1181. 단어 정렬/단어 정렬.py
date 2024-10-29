n = int(input())
set = set()

for _ in range(n):
    set.add(input())

lst = list(set)
lst.sort()
lst.sort(key=lambda x: len(x))

for word in lst:
    print(word)