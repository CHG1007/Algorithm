from itertools import permutations


def check(lst):
    ans = 0
    for num in permutations(lst, len(lst)):
        tmp = ''
        for n in num:
            tmp += ''.join(str(n))
        if int(tmp)%3 == 0:
            ans = int(tmp)
            break
    print(tmp)


n = list(map(int, input()))
n.sort(reverse=True)

if 0 not in n:
    print('-1')
elif sum(n)%3 != 0:
    print('-1')
else:
    check(n)