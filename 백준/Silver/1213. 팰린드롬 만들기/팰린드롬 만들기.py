name = input() # Ex) AAAABBC

count = dict()
keys = sorted(list(set(name)))
odd = []
for key in keys:
    cnt = name.count(key)
    count[key] = cnt
    if cnt % 2:
        odd.append(key)

if len(odd) > 1:
    print("I'm Sorry Hansoo")

else:
    result = ''

    for key in keys: # Ex) AAB 생성
        result += key * (count[key] // 2)

    if odd: # Ex) AAB += C + BAA
        result += odd[0] + result[::-1]
    else: # Ex)AAB += BAA
        result += result[::-1]

    print(result)