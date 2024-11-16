#   암호 만들기  골드 5

# n: 선택 횟수, c: 모음 갯수, tst: 현재까지 선택한 문자열
def dfs(n, cnt, tst):
    # c개의 문자들을 다 포함할지 안할지 선택했다면
    if n == c:
        # 문자열의 길이가 l, 모음갯수, 자음갯수 만족 여부
        if len(tst) == l and cnt >= 1 and l-cnt >= 2:
            ans.append(tst)
        return

    dfs(n+1, cnt+check[ord(lst[n])], tst+lst[n])    # 선택 하는 경우
    dfs(n+1, cnt, tst)                              # 선택 하지 않는 경우


l, c = map(int, input().split())
lst = input().split()
lst.sort()  # 사전순

ans = []    # 정답 리스트
check = [0]*126     # 모음 판별 리스트
for ch in 'aeiou':
    check[ord(ch)] = 1

dfs(0, 0, "")
for st in ans:
    print(st)
