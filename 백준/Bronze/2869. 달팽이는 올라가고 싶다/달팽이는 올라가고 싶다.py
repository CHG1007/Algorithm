a, b, v = map(int, input().split())
one_day = a-b
final_m = v-a

if final_m % one_day == 0:
    ans = int(final_m//one_day) + 1
else:
    ans = int(final_m // one_day+1) + 1

print(ans)