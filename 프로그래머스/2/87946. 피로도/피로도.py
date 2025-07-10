def solution(k, dungeons):
    global answer, cnt
    answer = 0
    
    visited = [False] * len(dungeons)

    def recur(cur_k, cnt):
        global answer
        answer = max(answer, cnt)
        
        for i in range(len(dungeons)):
            if (visited[i] == False) & (dungeons[i][0] <= cur_k) :
                visited[i] = True
                recur(cur_k - dungeons[i][1], cnt+1)
                visited[i] = False
            
    recur(k, 0)            
    
    return answer