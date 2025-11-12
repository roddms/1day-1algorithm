from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    MAX = 102
    
    maps = [[0]*MAX for _ in range(MAX)]
    dist = [[-1]*MAX for _ in range(MAX)]
    
    for x1, y1, x2, y2 in rectangle:
        X1, Y1, X2, Y2 = x1*2, y1*2, x2*2, y2*2
        for x in range(X1, X2+1):
            for y in range(Y1, Y2+1):
                maps[x][y] = 1
                
    for x1, y1, x2, y2 in rectangle:
        X1, Y1, X2, Y2 = x1*2, y1*2, x2*2, y2*2
        for x in range(X1+1, X2):
            for y in range(Y1+1, Y2):
                maps[x][y] = 0
                
    sx,sy = characterX*2, characterY*2
    ex,ey = itemX*2, itemY*2
    
    q = deque([(sx,sy)]) # 현재 위치
    dist[sx][sy] = 1
    
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    
    while q:
        cx, cy = q.popleft()
        
        if cx == ex and cy == ey:
            return dist[cx][cy]//2
        
        for dx, dy in dirs:
            nx = cx + dx
            ny = cy + dy
            if 0<=nx<=MAX and 0<=ny<=MAX:
                if maps[nx][ny]==1 and dist[nx][ny]==-1:
                    q.append((nx,ny))
                    dist[nx][ny] = dist[cx][cy]+1        
    
    
    return -1