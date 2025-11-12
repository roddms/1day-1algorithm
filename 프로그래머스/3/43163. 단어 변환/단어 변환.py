from collections import deque

def solution(begin, target, words):
    answer = 0
    visited = []
    
    def one_diff(a,b):
        cnt = 0
        for x,y in zip(a,b):
            if x!=y:
                cnt+=1
                
        return cnt==1
    
    q = deque()
    q.append((begin,0))
    visited.append(begin)
    
    while q:
        cur_w,step = q.popleft()
        
        if cur_w == target:
            return step
        
        for nxt_w in words:
            if nxt_w not in visited and one_diff(nxt_w, cur_w):
                visited.append(nxt_w)
                q.append((nxt_w,step+1))
    
    return 0