def solution(n):
    arr = []
    ans = 0
    
    while(n > 0) :
        arr.append(n%10)
        n //= 10
        
    arr.sort(reverse=True)
    
    for num in arr :
        ans = ans * 10 + num
    
    return ans