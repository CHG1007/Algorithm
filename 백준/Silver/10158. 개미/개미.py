import sys
intput = sys.stdin.readline


w, h = map(int, input().split())
x, y = map(int, input().split())
t = int(input())

cnt_x, cnt_y = (t+x)//w, (t+y)//h

cor_x, cor_y = (t+x)%w, (t+y)%h

if cnt_x % 2 == 0:
    x = cor_x
else:
    x = w-cor_x

if cnt_y % 2 == 0:
    y = cor_y
else:
    y = h-cor_y

print(x, y)