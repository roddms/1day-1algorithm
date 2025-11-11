from collections import deque

def solution(begin, target, words):
    
    def diff_cnt(w1, w2):
        cnt = 0
        for x,y in zip(w1,w2):
            if x!=y:
                cnt+=1
        
        return cnt == 1
    
    q = deque([(begin, 0)])
    visited = [begin]
    
    while q:
        cur_w, step = q.popleft()
        
        if cur_w == target:
            return step
        
        for w in words:
            if w not in visited and diff_cnt(cur_w, w):
                visited.append(w)
                q.append((w, step+1))
    
    return 0