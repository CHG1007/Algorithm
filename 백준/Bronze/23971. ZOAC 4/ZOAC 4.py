h, w, n, m = map(int, input().split())

row, col = 0, 0

if h%(n+1) == 0:
    row = h//(n+1)
else:
    row = h // (n + 1) + 1

if w%(m+1) == 0:
    col = w//(m+1)
else:
    col = w // (m + 1) + 1

print(row*col)