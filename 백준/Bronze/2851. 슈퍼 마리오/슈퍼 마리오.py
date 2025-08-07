#   슈퍼 마리오  브론즈 1


# 입력 처리
lst = []
for _ in range(10):
    lst.append(int(input()))

# 누적합 배열 생성
prefix_sum = [0]*10
prefix_sum[0] = lst[0]
idx = 9

# 누적합 배열 할당
for i in range(1, 10):
    prefix_sum[i] = prefix_sum[i-1]+lst[i]

for i in range(10):
    if i == 0 and prefix_sum[i] >= 100:
        idx = 0
        break
    elif prefix_sum[i] >= 100:
        idx = i
        break


if idx == 0:
    print(prefix_sum[idx])
else:
    if abs(prefix_sum[idx]-100) <= abs(prefix_sum[idx-1]-100):
        print(prefix_sum[idx])
    else:
        print(prefix_sum[idx-1])














