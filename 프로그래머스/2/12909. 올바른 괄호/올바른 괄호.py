def solution(s):
    
    stack = []
    for c in s :
        if c == '(':
            stack.append('(')
        else:
            if not stack: # 비어있는 stack 이면 False 반환
                return False
            stack.pop()   # 비어있지 않으면 (닫힌 괄호이면) 삭제

    return not stack