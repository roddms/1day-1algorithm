# Bottom-Up
N, M = map(int, input().split())

# 각 방의 사탕 개수가 있는 arr 생성
arr = [[0] + list(map(int, input().split())) for _ in range(N)]
arr = [[0] * (M+1)] + arr

dp = [ [0 for _ in range(M+1)] for _ in range(N+1)]
dp[1][1] = arr[1][1]

# 첫 행, 첫 열의 값은 미리 생성해 둠
for i in range(2, N+1):
    dp[i][1] = arr[i][1] + dp[i-1][1]

for j in range(2, M+1):
    dp[1][j] = arr[1][j] + dp[1][j-1]

# 나머지 위치는 점화식
for i in range(2, N+1):
    for j in range(2, M+1):
        dp[i][j] = arr[i][j] + max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

print(dp[N][M])
