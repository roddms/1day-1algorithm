import sys
sys.setrecursionlimit(1000000)

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
arr = [[0, 0, 0]] + arr

dp  = [ [-1 for _ in range(3)] for _ in range(N+1)]

# 첫 번째 집의 비용은 미리 넣어둠
for i in range(3):
    dp[0][i] = arr[0][i]

# color : R 0, G 1, B 2

def recur(n, color):
    global arr, dp

    if n == 0:
        return dp[0][color]

    if n>=1 and dp[n][color] != -1:
        return dp[n][color]
    
    if color == 0:   # R
        dp[n][0] = arr[n][0] + min(recur(n-1, 1), recur(n-1, 2))
    elif color == 1: # G
        dp[n][1] = arr[n][1] + min(recur(n-1, 0), recur(n-1, 2))
    else:            # B
        dp[n][2] = arr[n][2] + min(recur(n-1, 0), recur(n-1, 1))
    
    return dp[n][color]

cost_R = recur(N, 0)
cost_B = recur(N, 1)
cost_G = recur(N, 2)

print(min(cost_R, cost_B, cost_G))