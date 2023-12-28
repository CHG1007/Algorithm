T = int(input())    # 테스트 케이스

for tc in range(T):
    N = int(input())    # 통나무 갯수
    lst = list(map(int, input().split()))   # 통나무 높이
    lst_2 = [0]*N
    ans = 0

    lst.sort()

    for i in range(0, N//2):
        lst_2[i] = lst[i*2]
        lst_2[N-i-1] = lst[i*2+1]

    if N % 2 == 1:
        lst_2[N//2] = lst[-1]

    for i in range(0, N):
        ans = max(ans, abs(lst_2[i-1]-lst_2[i]))

    print(ans)