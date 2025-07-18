N = int(input())

d = [0] * (N+1)

# 맨  처음 두 자리는 1, 0으로 고정하고 시작
d[0] = 0
d[1] = 1

for i in range(2, N+1):
    d[i] = d[i-2] + d[i-1]

print(d[N])