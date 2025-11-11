from collections import deque

def solution(n, computers):
    ans = 0
    visited = [False] * n

    for start in range(n):
        if visited[start] == True:
            continue
            
        ans += 1
        visited[start] = True
        
        q = deque([start])
        
        while q:
            cur = q.popleft()
            for nxt in range(n):
                if computers[cur][nxt]==1 and visited[nxt]==False:
                    visited[nxt] = True
                    q.append(nxt)
    
    return ans