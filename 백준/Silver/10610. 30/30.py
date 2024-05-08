lst = input()
n = list(map(int, lst))
lst = sorted(list(lst), reverse=True)

# n에 0이 없거나, 합이 3의 배수가 아닌경우 즉시 종료
if 0 not in n:
    print('-1')
elif sum(n)%3 != 0:
    print('-1')
else:
    # check(n)
    print(''.join(lst))