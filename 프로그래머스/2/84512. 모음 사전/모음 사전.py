def solution(word):
    v = ['A', 'E', 'I', 'O', 'U']
    answer = 0
    cnt = 0
    
    def dfs(cur): # cur : 현재 만든 단어
        nonlocal answer, cnt
        
        if cur:
            cnt += 1
            if cur == word:
                answer = cnt
                return
            
        if len(cur) == 5:
            return
        
        for ch in v:
            if answer != 0:
                return 
            dfs(cur+ch)
        
    dfs("")
    return answer