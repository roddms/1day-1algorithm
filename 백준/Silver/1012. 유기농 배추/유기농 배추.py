# 안전영역 문제랑 똑같음
from collections import deque

T = int(input())

dy = [-1, 0, 1, 0]
dx = [0, -1 , 0, 1]

for _ in range(T):

    ans = 0
    M, N, K = map(int, input().split())

    baechu = [[False] * (M) for _ in range(N)]  # 배추 위치 저장
    visited = [[False] * (M) for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        baechu[y][x] = True

    def bfs(sy, sx):
        q = deque()
        q.append((sy, sx))
        visited[sy][sx] = True
        
        while q:
            y, x = q.popleft()
        
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                
                if (0 <= ny < N and 0 <= nx < M) and (baechu[ny][nx]) and (not visited[ny][nx]):
                    q.append((ny, nx))
                    visited[ny][nx] = True

    for y in range(N):
        for x in range(M):
            if (baechu[y][x]) and (not visited[y][x]):
                bfs(y, x)
                ans += 1

    print(ans)