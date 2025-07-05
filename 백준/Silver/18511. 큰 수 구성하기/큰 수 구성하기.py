N, k = map(int, input().split())
K = list(map(int, input().split()))
K.sort()

choose = []
lim = 0

def comb(level, max_level):
    global choose, lim

    if 1 <= level <= max_level:
        num = 0
        for digit in choose:
            num = num * 10 + digit
        if num <= N:
            lim = max(lim, num)

    if level == max_level:
        return

    for i in range(k):  # k는 K의 길이
        choose.append(K[i])
        comb(level + 1, max_level)
        choose.pop()

# 자릿수 1 ~ len(str(N))까지 모두 탐색
for digits in range(1, len(str(N)) + 1):
    comb(0, digits)

print(lim)