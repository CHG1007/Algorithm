import re

# 입력 식을 숫자와 연산 기호로 분리하기(앞에 0이 붙는 숫자 0제거)
lst = input()
lst = re.split('([-|+])', lst)
Str = ''
for data in lst:
    if data == '+':
        Str += ''.join(data)
    elif data == '-':
        Str += ''.join(data)
    else:
        Str += ''.join(str(int(data)))

# '-'를 기준으로 식을 나눈후
Str = Str.split('-')
Sum = 0

for i in range(len(Str)):
    if i == 0:
        # 첫째항만 덧셈
        Sum += eval(Str[i])
    else:
        # 이후항은 뺄셈계산
        Sum -= eval(Str[i])

print(Sum)