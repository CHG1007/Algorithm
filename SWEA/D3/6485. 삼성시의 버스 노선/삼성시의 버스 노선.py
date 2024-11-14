#   삼성시의 버스 노선 D3   5:23 >> 5:31


t = int(input())

for tc in range(t):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    p = int(input())
    staion = [int(input()) for _ in range(p)]

    ans = []
    # 모든 버스 정류장에 대해
    for num in staion:
        cnt = 0     # 각 정류장에 다니는 버스 노선 갯수
        # 모든 노선에 대해
        for data in lst:
            # 노선 범위에 포함되면 카운트 추가
            if data[0] <= num <= data[1]:
                cnt += 1
        ans.append(cnt)

    print(f'#{tc+1}', end=' ')
    print(*ans)
