a, b = map(str, input().split())

a = a[::-1]
b = b[::-1]

a_n = ''.join(a)
b_n = ''.join(b)

if int(a_n) > int(b_n):
    print(int(a_n))
else:
    print(int(b_n))

