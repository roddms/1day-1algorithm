def solution(citations):
    answer = 0
    
    citations.sort(reverse=True) # 6, 5, 3, 1, 0
    
    # 내림차순 정렬한 피인용수 순서대로 인덱스 잡고 인덱스와 피인용수가 같아지는 지점이 answer
    for i in range(len(citations)):
        if citations[i] >= i+1:
            answer = i+1
    
    return answer