#   donstructive    실버 4


# 입력 처리
N = int(input().strip())
odds = list(range(1, N+1, 2))           # 홀수 배열
evens = list(range(2, N+1, 2))[::-1]    # 짝수 배열
ans = odds + evens
# print(odds, evens)
# 정답 출력
print(*ans)

