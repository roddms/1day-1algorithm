#14501
N = int(input())
schedule = [list(map(int, input().split())) for _ in range(N)]
ans = 0

def recur(idx, p):
    global ans

    if idx >= N:
        ans = max(p, ans)
        return

    # 상담
    if idx + schedule[idx][0] <= N:
        recur(idx+schedule[idx][0],p+schedule[idx][1])

    # 상담 X
    recur(idx+1, p)

recur(0,0)
print(ans)