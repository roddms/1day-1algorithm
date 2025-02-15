def solution(num):
    ans = 0
    
    while (num != 1) :
        if num % 2 == 0 :
            num /= 2
            ans += 1
            if ans>=500 :
                ans = -1
                break
        else :
            num = num*3 +1
            ans += 1
            if ans>=500 :
                ans = -1
                break
    
    return ans