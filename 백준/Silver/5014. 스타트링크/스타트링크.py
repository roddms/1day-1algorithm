from collections import deque

F, S, G, U, D = map(int, input().split())

q = deque()
visited = [False] * (F+1)

q.append((0, S)) # 지금까지 버튼 누른 횟수, 현재 위치
visited[S] = True

while q:
    
    cnt, cur = q.popleft()

    if cur == G:
        print(cnt)
        exit()

    for nxt in [cur+U, cur-D]:
        if (1<= nxt <= F) and (not visited[nxt]):
            q.append((cnt+1, nxt))
            visited[nxt] = True

print("use the stairs")