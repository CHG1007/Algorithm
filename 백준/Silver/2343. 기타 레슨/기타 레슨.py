def search(limit):
    count = 1   # 블루레이 개수
    total = 0   # 현재 블루레이에 누적된 강의 시간

    for time in lst:
        # 강의가 현재 블루레이에 들어갈 수 없으면 새 블루레이 사용
        if total + time > limit:
            count += 1      # 블루레이 하나 추가
            total = time    # 새 블루레이에 강의 저장
        # 강의가 현재 블루레이에 들어갈 수 있으면 현재 블루레이에 저장
        else:
            total += time

    # 총 사용한 블루레이가 m이하면 가능
    if count <=m :
        return True
    else:
        return False


# 입력 처리
n, m = map(int, input().split())
lst = list(map(int, input().split()))

# 이분 탐색 범위 설정
low = max(lst)      # 블루레이 최소 용량(가장 긴 강의)
high = sum(lst)     # 블루레이 최대 용량(모두 한 개에 담는 경우)
result = high       # 초기값 설정

while low <= high:
    mid = (low+high)//2

    # 가능한 경우, 더 작은 용량도 가능한지 탐색
    if search(mid):
        result = mid
        high = mid-1
    # 불가능하다면 용량 늘리기
    else:
        low = mid+1

print(result)