import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort(reverse=True)
MOD = 10**9+7   # 출력 시 사용할 모듈값 (문제 조건: p × q + r 중 r만 출력)

# 1,2번째로 큰 마력석
maxA, secondMaxA = lst[0], lst[1]

# 마력석 N번 합성
for _ in range(n):
    # 가장 큰 두 마력석을 합성하여 새 마력석 생성
    newA = maxA + secondMaxA

    # 가장 큰 값이 음수인 경우(0포함) 앞으로 생성된 마력석은 그보다 작으므로 계산 불필요
    if maxA <= 0:
        break
    else:
        # 새로운 마력석이 가장 큰 경우
        if maxA <= newA:
            secondMaxA = maxA
            maxA = newA
        # 새로운 마력석이 두번째로 큰 경우
        elif secondMaxA < newA:
            secondMaxA = newA

        # 각 값을 모듈러 처리
        if maxA > MOD and secondMaxA > MOD:
            maxA = maxA % MOD
            secondMaxA = secondMaxA % MOD

# 마지막에 생성된 마력석의 마나 수치를 출력
# 단, 음수가 될 수 있으므로 MOD 더한 후 % MOD 처리
print((newA + MOD) % MOD)