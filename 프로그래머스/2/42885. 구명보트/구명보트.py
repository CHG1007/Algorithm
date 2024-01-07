def solution(people, limit):
    answer = 0
    N = len(people)
    people.sort()

    L = 0
    R = N - 1

    while L <= R:
        Sum = people[L] + people[R]
        if Sum <= limit:
            L += 1
        R -= 1
        answer += 1

    print(answer)
    return answer