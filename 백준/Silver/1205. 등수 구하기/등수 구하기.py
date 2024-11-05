import sys
input = sys.stdin.readline


def rank():
    # 랭킹 리스트에 올라 갈 수 있으면 >> 점수 리스트에 등록
    if n < p:
        lst.append(score)
    # 랭킹 리스트가 꽉 찼다면
    else:
        # 현재 리스트의 가장 낮은 점수보다 좋은 점수라면 등록
        if lst[-1] < score:
            lst.pop()
            lst.append(score)
        # 현재 리스트의 가장 낮은 점수보다 낮은 점수라면 불가
        else:
            return -1
    # 등수는 같은 점수가 있을때 그러한 점수의 등수 중 가장 작은 등수
    return sorted(lst, reverse=True).index(score)+1


n, score, p = map(int, input().split())
lst = []    # 현재 랭킹 리스트

# n이 0보다 큰 경우메만 입력 주어짐
if n > 0:
    tmp = list(map(int, input().split()))
    for num in tmp:
        lst.append(num)

print(rank())