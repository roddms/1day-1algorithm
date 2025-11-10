from collections import deque

def solution(numbers, target):
    answer = 0
    
    q = deque
    q = deque([(0, 0)]) # 인덱스, 현재까지의 합
    
    while q:
        idx, cur = q.popleft()
        
        if idx == len(numbers):
            if cur == target:
                answer += 1
            continue
        
        q.append((idx+1, cur+numbers[idx]))
        q.append((idx+1, cur-numbers[idx]))            
    
    return answer