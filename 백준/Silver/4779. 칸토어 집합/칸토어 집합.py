# 0 < N < 12
ans = ['' for _ in range(13)]

# 초기값 설정
ans[0] = '-'

for i in range(1, 13):
    ans[i] = ans[i-1] + (' ' * (3 ** (i-1))) + ans[i-1]

while True:
    try:
        N = int(input())
        print(ans[N])
    except:
        break