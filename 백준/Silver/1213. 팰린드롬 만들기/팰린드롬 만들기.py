lst = input()
count = dict()
keys = sorted(list(set(lst)))
odd = []

for key in keys:
    cnt = lst.count(key)
    count[key] = cnt
    if cnt%2 == 1:
        odd.append(key)

if len(odd) > 1:
    print("I'm Sorry Hansoo")
else:
    ans = ''

    for key in keys:
        ans += key*(count[key]//2)

    if odd:
        ans += odd[0] + ans[::-1]
    else:
        ans += ans[::-1]

    print(ans)