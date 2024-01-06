import itertools


# 소수 판별 함수
def prime(num):
    cnt = 0

    for i in range(1, num+1):
        if num % i == 0:
            cnt += 1
        if cnt > 2:
            return False

    if cnt == 2:
        return True


def solution(numbers):
    answer = 0
    num = [int(x) for x in numbers]
    num_set = set()
    N = len(num)

    # 종이 조각 1개~N개 사용하여 만들 수 있는 모든 수
    for i in range(1, N+1):
        for part in itertools.permutations(num, i):
            number = ""
            for j in range(len(part)):
                number += str(part[j])
            num_set.add(int(number))

    for data in num_set:
        if prime(data):
            answer += 1

    return answer