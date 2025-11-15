def solution(brown, yellow):
    answer = []
    tot = brown + yellow
    
    for h in range(3, tot):
        
        if tot % h == 0:
            w = tot // h
            if w >= h:
                if (w-2) * (h-2) == yellow:
                    answer.append(w)
                    answer.append(h)
                    break
    
    return answer