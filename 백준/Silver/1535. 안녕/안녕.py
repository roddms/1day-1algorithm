N = int(input())

L = list(map(int, input().split()))
J = list(map(int, input().split()))

# 체력이 l일때의 최대 기쁨
dp = [[-1 for _ in range(101)] for _ in range(N+1)]

def recur(idx, l):
        
    # 만약 체력을 다 썼다면
    if l <= 0 :
        return -9999999999
    
    # 끝까지 다 돌았으면 더 이상 더할 기쁨 없음 = 0
    if idx == N:
        return 0
    
    # 이미 계산된 값이 있다면
    if dp[idx][l] != -1:
        return dp[idx][l]

    dp[idx][l] = max(recur(idx+1, l-L[idx])+J[idx], recur(idx+1, l))

    return dp[idx][l]

print(recur(0,100))
