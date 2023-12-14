import itertools

n, m = map(int, input().split())    # 자연수 N, M

lst =list(range(1,n+1))

for combi in itertools.permutations(lst, m):
    print(*combi)