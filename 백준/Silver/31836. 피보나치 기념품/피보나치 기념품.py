#   피보나치 기념품    실버 1

import sys
input = sys.stdin.readline

# 입력 처리
N = int(input().strip())

serim = []   # 세림(인덱스)
seong = []   # 성주(인덱스)

if N == 2:
    # F1=1, F2=1 → 1개씩
    serim.append(1)
    seong.append(2)
else:
    r = N % 3

    if r == 0:
        # 전부 3개씩 소거: (세림){k-1,k-2}, (성주){k}
        k = N
        while k >= 3:
            serim.extend([k-1, k-2])
            seong.append(k)
            k -= 3

    elif r == 2:
        if N == 5:
            # 시드만으로 완성: 세림[1,3,4], 성주[2,5]
            serim.extend([1, 3, 4])
            seong.extend([2, 5])
        else:
            # 시드 배치 후(합=6=6) 나머지 3개씩 소거
            serim.extend([1, 3, 4])  # {1,2,3}
            seong.extend([2, 5])     # {1,5}
            k = N
            while k >= 6:
                serim.extend([k-1, k-2])
                seong.append(k)
                k -= 3

    else:
        # r == 1: 인덱스 1 하나만 제외하고 3개씩 소거
        k = N
        while k >= 3:
            # 묶음에 1이 섞이면 한 칸 내려서 재구성
            if k == 1 or k-1 == 1 or k-2 == 1:
                k -= 1
                continue
            serim.extend([k-1, k-2])
            seong.append(k)
            k -= 3

# 출력 형식: 번호 오름차순
serim.sort()
seong.sort()

print(len(serim))
print(*serim)
print(len(seong))
print(*seong)
