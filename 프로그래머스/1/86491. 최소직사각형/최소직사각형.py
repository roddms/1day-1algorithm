def solution(sizes):
    answer = 0
    
    # 모든 명함의 0번 자리에 더 긴 부분이 오도록 정렬
    sizes = [(max(w, h), min(w, h)) for w, h in sizes]
    
    # 아래 방식은 sizes는 결국 안 바뀌고 루프 내에서만 바뀜
    # for w, h in sizes:
    #     if w < h:
    #         w, h = h, w
            
    max_w = max(w for w, h in sizes)
    max_h = max(h for w, h in sizes)
    
    answer = max_w * max_h
            
    return answer