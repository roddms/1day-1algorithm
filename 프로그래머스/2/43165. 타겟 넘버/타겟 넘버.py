# dfs
def solution(numbers, target):
    
    def dfs(idx, cur):
        nonlocal answer
        
        if idx == len(numbers):
            if cur == target:
                answer += 1
            
        else:
            dfs(idx+1, cur+numbers[idx])
            dfs(idx+1, cur-numbers[idx])
    
    answer = 0
    
    dfs(0,0)
    
    return answer