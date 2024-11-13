for tc in range(10):
    ans = 0
    n = int(input())
    lst = list(map(int, input().split()))

    for i in range(2, n-2):
        c = lst[i]  # 현재 빌딩 높이
        # 좌 우 2칸씩 현재 빌딩 높이와 차이 계산후 최소값 저장
        cnt = min(c-lst[i-2], c-lst[i-1], c-lst[i+1], c-lst[i+2])
        
        # 최소값 0 이상 >> 조망권 만족 >> 갯수 누적
        if cnt > 0:
            ans += cnt

    print(f'#{tc+1} {ans}')