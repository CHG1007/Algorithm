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
        lst.remove(n)
    else:
        lst.append(n)


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

    f = oper[0]
    if f == 'add':
        add(int(oper[1]))
    elif f == 'remove':
        remove(int(oper[1]))
    elif f == 'check':
        check(int(oper[1]))
    elif f == 'toggle':
        toggle(int(oper[1]))
    elif f == 'all':
        all()
    elif f == 'empty':
        empty()