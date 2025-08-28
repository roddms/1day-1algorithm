def solution(brown, yellow):
    answer = []
    size = brown + yellow  # 전체 카펫 면적

    for h in range(1, int(size**0.5) + 1):
        if size % h == 0:   # h : height 후보
            w = size // h   # w : width 후보
            if (w - 2) * (h - 2) == yellow:  # 노란색 조건
                answer = [w, h] if w >= h else [h, w]
                break

    return answer
