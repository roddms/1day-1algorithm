from collections import deque

def solution(n, wires):
    answer = n
    adj_lst = [[] for _ in range(n+1)]
    
    for a, b in wires:
        adj_lst[a].append(b)
        adj_lst[b].append(a)
    
    def bfs(start, cut_a, cut_b):
        visited = [False] * (n+1)
        
        q = deque()
        q.append(start)
        visited[start] = True
        cnt = 1
        
        while q:
            cur = q.popleft()
            for nxt in adj_lst[cur]:
                if (cur == cut_a and nxt == cut_b) or (cur == cut_b and nxt == cut_a):
                    continue
                if visited[nxt] == False:
                    visited[nxt] = True
                    q.append(nxt)
                    cnt += 1
                    
        return cnt
    
    for a, b in wires:
        count = bfs(a, a, b)
        diff = abs(2*count - n)
        answer = min(diff, answer)
    
    return answer