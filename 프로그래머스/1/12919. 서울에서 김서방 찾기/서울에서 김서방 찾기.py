def solution(seoul):
    answer = ''
    
    for i in range(0, len(seoul)+1) :
        if seoul[i] == 'Kim' :
            answer = i
            break;
    
    return f"김서방은 {answer}에 있다"