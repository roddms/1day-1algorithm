from collections import deque

N, K = map(int, input().split())

q = deque()
visited = [False] * (100001)


q.append((0, N)) # time, 현재 위치
visited[N] = True

while q:

    time, cur = q.popleft()

    if cur == K:
        print(time)
        exit()

    
    for nxt in [cur-1, cur+1, cur*2]:
        if (0 <= nxt <= 100000) and (not visited[nxt]):
            q.append((time+1, nxt))
            visited[nxt] = True