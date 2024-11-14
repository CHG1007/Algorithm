#   숫자 조작 D3    4:40 >>


t = int(input())

for tc in range(t):
    n = list(input())

    max_n = int(''.join(n))     # 최대값
    min_n = int(''.join(n))     # 최소값

    # 정수n 중 한 쌍의 숫자를 골라 위치를 바꾸는 모든 경우에 대해
    for i in range(len(n)-1):
        for j in range(1, len(n)):
            # 가장 앞자리가 0인 경우 제외
            if i == 0 and n[j] == '0':
                continue
            n[i], n[j] = n[j], n[i]     # 자리 바꾸기
            max_n = max(max_n, int(''.join(n)))     # 바꾼값 중 최대값 갱신
            min_n = min(min_n, int(''.join(n)))     # 바꾼값 중 최소갑 갱신
            n[i], n[j] = n[j], n[i]     # 자리 원위치

    print(f'#{tc+1} {min_n} {max_n}')
