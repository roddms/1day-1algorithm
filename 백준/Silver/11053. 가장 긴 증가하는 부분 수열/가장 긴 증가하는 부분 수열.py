N = int(input())
arr = [0] + list(map(int, input().split()))

# dp[i] : arr[i]로 끝나는 부분 수열의 길이
dp = [-1] * (N+1)

dp[1] = 1

for n in range(2, N+1):
    best = 0
    for i in range(1,n):
        if arr[n] > arr[i]:
            best = max(best, dp[i])
    dp[n] = best + 1

print(max(dp))