def password():
    # 1. 모음 포함 조건
    cnt = 0
    for vo in vowel:
        if vo in lst:
            cnt += 1
            break
    if cnt == 0:
        return False

    # 2. 모음 3개 혹은 자음3개 연속 조건
    cnt_c, cnt_v = 0, 0
    for s in lst:
        if s in con:
            cnt_c += 1
            cnt_v = 0
        else:
            cnt_v += 1
            cnt_c = 0
        if cnt_c >= 3 or cnt_v >= 3:
            return False

    # 3. 같은 글자가 연속적으로 두번 오면 안되나, ee와 oo는 허용한다
    for i in range(1, len(lst)):
        if lst[i-1] == lst[i]:
            if lst[i-1] != 'e' and lst[i-1] != 'o':
                return False

    return True


vowel = ['a', 'e', 'i', 'o', 'u']   # 모음

con = [chr(x+97) for x in range(ord('z')-ord('a')+1)]   # 자음
for v in vowel:
    con.remove(v)

while True:
    word = input()
    lst = list(word)

    if word == 'end':
        break

    if password():
        print(f'<{word}> is acceptable.')
    else:
        print(f'<{word}> is not acceptable.')
