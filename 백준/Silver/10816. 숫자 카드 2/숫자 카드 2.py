# BOJ 10816 숫자 카드 2 - 딕셔너리 카운팅 정석 풀이

import sys
input = sys.stdin.readline

# 1) 입력
N = int(input())
card = list(map(int, input().split()))
M = int(input())
check_card = list(map(int, input().split()))

# 2) 상근이 카드의 '값 -> 개수'를 해시맵(딕셔너리)로 저장
count = {}
for x in card:
    # count[x]가 없으면 0으로 보고 +1
    count[x] = count.get(x, 0) + 1

# 3) 질의 값에 대해 카운트를 조회하여 결과 문자열로 모음
#    (반복 print 대신 join으로 한 번에 출력 → IO 비용 절감)
res = [str(count.get(x, 0)) for x in check_card]

# 4) 출력
print(' '.join(res))
