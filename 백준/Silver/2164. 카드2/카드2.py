from collections import deque

n = int(input())       # n: 카드 수

# 1부터 N까지의 카드들
deque = deque(range(1, n+1))

while len(deque) > 1:               # 카드가 한장 남을때까지 반복
    deque.popleft()                 # 가장 위에 카드를 버리고
    deque.append(deque.popleft())   # 그 다음 위에있던 카드를 가장 아래로 이동

print(*deque)