def solution(n, k):
    
    if n >= 10 and k > n/10 :
        ans = 12000*n + 2000*(k-n//10)
        
    elif n >= 10 and k <= n/10 :
        ans = 12000*n + 2000*(k-n//10)
        
    else :
        ans = 12000*n + 2000*k
    
    return ans