while True:
    lst = list(map(int, input().split()))
    lst.sort()
    a, b, c = lst[0], lst[1], lst[2]
    if a==0 and b==0 and c==0:
        break

    if a+b <= c:
        print('Invalid')
    elif a==b and b==c:
        print('Equilateral ')
    elif a != b and b != c and a != c:
        print('Scalene ')
    else:
        print('Isosceles ')