#   직사각형    실버 1


# 입력 처리
for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    ans = ''
    # 1. 전혀 겹치지 않는 경우 (d)
    if p1<x2 or p2<x1 or q1<y2 or q2<y1:
        ans = 'd'

    # 2. 한 점에서 만나는 경우 (c)
    elif (p1==x2 and q1==y2) or (x1==p2 and y1==q2) or (p1==x2 and y1==q2) or (x1==p2 and y2==q1):
        ans = 'c'

    # 3. 한 선분에서 만나는 경우 (b)
    elif p1==x2 or x1==p2:
        ans = 'b'
    elif q1==y2 or y1==q2:
        ans = 'b'

    # 4. 겹치는 넓이가 있는 경우 (a)
    else:
        ans = 'a'

    print(ans)
