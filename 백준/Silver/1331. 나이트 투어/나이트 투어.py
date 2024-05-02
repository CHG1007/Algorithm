dic = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6}
order = []
visit = []

for i in range(36):
    data = input()
    order.append([dic[data[0]] - 1, int(data[1]) - 1])

flag = True
for i, j in order:
    # move(i, j)
    if [i, j] in visit:
        flag = False
        break
    visit.append([i, j])

for i in range(1, 36):
    flag2 = False
    for dx, dy in ((-2, -1), (-2, 1), (-1, 2), (1, 2), (2, -1), (2, 1), (-1, -2), (1, -2)):
        if order[i - 1][0] + dx == order[i][0] and order[i - 1][1] + dy == order[i][1]:
            flag2 = True
    if flag2 == False:
        break

flag3 = False
for dx, dy in ((-2, -1), (-2, 1), (-1, 2), (1, 2), (2, -1), (2, 1), (-1, -2), (1, -2)):
    if order[-1][0] + dx == order[0][0] and order[-1][1] + dy == order[0][1]:
        flag3 = True

if flag and flag2 and flag3:
    print('Valid')
else:
    print('Invalid')