def solution(k, dungeons):
    ans = 0
    visited = [False]*len(dungeons)
    
    def dfs(cur, cnt): # 현재 피로도, 현재 방문 횟수
        nonlocal ans
        
        if cnt > ans:
            ans = cnt
        
        for i in range(len(dungeons)):
            if cur >= dungeons[i][0] and not visited[i]:
                visited[i]=True
                dfs(cur-dungeons[i][1], cnt+1)
                visited[i] = False
                
    dfs(k,0)
    return ans