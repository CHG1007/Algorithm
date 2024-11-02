import sys
input = sys.stdin.readline


def add(n):
    if n not in lst:
        lst.append(n)


def remove(n):
    if n in lst:
        lst.remove(n)


def check(n):
    if n in lst:
        print(1)
    else:
        print(0)


def toggle(n):
    if n in lst:
        remove(n)
    else:
        add(n)


def all():
    global lst
    lst = list(range(1, 21))


def empty():
    global lst
    lst = []


m = int(input())
lst = []
for _ in range(m):
    oper = list(input().split())
    if len(oper)>=2:
        num = oper[1]
    
    f = oper[0]
    if f == 'add':
        add(int(num))
    elif f == 'remove':
        remove(int(num))
    elif f == 'check':
        check(int(num))
    elif f == 'toggle':
        toggle(int(num))
    elif f == 'all':
        all()
    elif f == 'empty':
        empty()
