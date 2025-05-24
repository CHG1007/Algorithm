#   일곱 난쟁이  브론즈 1

import itertools

lst = [int(input()) for _ in range(9)]

for ans in itertools.combinations(lst, 7):
    ans = list(ans)
    ans.sort()
    if sum(ans) == 100:
        for dwarf in ans:
            print(dwarf)
        break
