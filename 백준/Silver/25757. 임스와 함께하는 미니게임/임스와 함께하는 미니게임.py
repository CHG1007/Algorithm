import sys
input = sys.stdin.readline


# game(player) >> 게임 명수가 player일때 플레이 가능한 게임 횟수 
def game(player):
    global n
    ans = 0
    l = len(q)
    
    # 플레이어 명단 수보다 게임 명수가 같거나 크다면 >> 게임 가능
    while l >= player:
        l -= player
        ans += 1
        n -= 1
        # 하지만 그 전에 신청 횟수를 만족 했다면 종료
        if n == 0:
            break
    print(ans)


n, g = input().split()
n = int(n)
q = set()
# 이름이 겹치지 않도록 set 에 누적
for _ in range(n):
    q.add(input())

if g == 'Y':
    game(1)
elif g == 'F':
    game(2)
else:
    game(3)