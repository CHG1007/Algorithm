def target():
    start = 1
    end = max(lst)

    while start <= end:
        mid = (start + end)//2
        total = 0

        for tree in lst:
            if tree >= mid:
                total += tree-mid

        if total >= m:
            start = mid + 1
        else:
            end = mid-1

    return end


n, m = map(int, input().split())
lst = list(map(int, input().split()))

print(target())