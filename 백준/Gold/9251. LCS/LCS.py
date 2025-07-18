s1 = input()
s2 = input()

N, M = len(s1), len(s2)
# 인덱스 1부터 시작하도록 앞에 공백 추가
s1 = " " + s1
s2 = " " + s2

# 초기값 처리
# dp[i][j] : s1[i]까지, s2[j]까지 순회했을 때의 LCS
dp = [[0] * (M + 1) for _ in range(N + 1)]

# dp[n][m]
for n in range(1, N + 1):
    for m in range(1, M + 1):
        if s1[n] == s2[m]: # 두 문자가 같다면 이전까지 LCS에 +1
            dp[n][m] = dp[n - 1][m - 1] + 1
        else:              # 두 문자가 다르다면 두 가지 선택지
                           # 1. s1[n-1]까지와 s2[m]까지의 LCS 길이
                           # 2. s1[n]까지와 s2[m-1]까지의 LCS 길이
            dp[n][m] = max(dp[n - 1][m], dp[n][m - 1])

print(dp[N][M])