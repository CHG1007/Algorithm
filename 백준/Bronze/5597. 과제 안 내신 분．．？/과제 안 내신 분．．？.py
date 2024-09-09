lst = [int(input()) for _ in range(28)]
student = list(range(1, 31))

print(*sorted(set(student)-set(lst)))