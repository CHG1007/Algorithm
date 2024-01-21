def dfs(si, sj, n):
    global ans

    for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni, nj = si+di, sj+dj
        if 0<=ni<R and 0<=nj<C and v[ord(arr[ni][nj])-A] == 0:
            v[ord(arr[ni][nj])-A] = 1
            dfs(ni, nj, n+1)
            v[ord(arr[ni][nj])-A] = 0

    ans = max(ans, n)


R, C = map(int, input().split())

arr = [input() for _ in range(R)]
A = ord('A')
v = [0]*A
v[ord(arr[0][0])-A] = 1
ans = 0

dfs(0, 0, 1)
print(ans)
