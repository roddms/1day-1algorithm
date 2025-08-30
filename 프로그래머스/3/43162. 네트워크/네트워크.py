def solution(n, computers):
    ans = 0
    visited = [False for _ in range(n)]
    
    def dfs(cur):
        visited[cur] = True
        
        for nxt in range(n):
            if computers[cur][nxt] and not visited[nxt]:
                dfs(nxt)
                
    for i in range(n):
        if not visited[i]:
            dfs(i)
            ans += 1
    
    return ans