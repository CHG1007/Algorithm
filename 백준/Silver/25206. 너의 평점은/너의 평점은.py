import sys

input = sys.stdin.readline

credit = ['A+','A0','B+','B0','C+','C0','D+','D0','F']
grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]

total, cnt = 0, 0

for _ in range(20):
    s, g, c = input().split()
    g = float(g)

    if c != 'P':
        cnt += int(g)
        total += g*grade[credit.index(c)]

print(total/cnt)