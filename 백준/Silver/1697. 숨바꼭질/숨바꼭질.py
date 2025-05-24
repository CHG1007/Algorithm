from collections import deque


def bfs(e):
    # 1. 큐생성
    q = deque()

    # 2. 방문 배열
    q.append(n)
    v = [0]*100001
    cnt = 0
    
    # 3. 순간이동 할지 걸을지
    while q:
        si = q.popleft()
        if si == e:
            print(v[e])
            break
        # 탐색 앞뒤로1칸 혹은 2배
        for di in (si-1, si+1, 2*si):
            if 0<=di<=100000 and v[di] == 0:
                v[di] = v[si]+1
                q.append(di)
            
             
    
n, m  = map(int, input().split())
bfs(m)


