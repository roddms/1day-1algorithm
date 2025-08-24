def solution(answers):
    score = [0] * 3
    answer = []
    
    # 각 수포자의 제출 답안 만들기
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    submit = [
        [p1[i % len(p1)] for i in range(len(answers))],
        [p2[i % len(p2)] for i in range(len(answers))],
        [p3[i % len(p3)] for i in range(len(answers))]
    ]
    
    # i번 수포자가 맞으면 score[i-1] += 1 식으로 점수 카운팅
    for j in range(3):
        for i in range(len(answers)):
            if answers[i] == submit[j][i]:
                score[j] += 1
        
        
    for i in range(3):
        if max(score) == score[i]:
            answer.append(i+1)
    
    answer.sort()
    
    return answer