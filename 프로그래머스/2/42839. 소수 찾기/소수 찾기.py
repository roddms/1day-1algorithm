from itertools import permutations

def solution(numbers):
    answer = 0
    comb = set()  # 중복 제거를 위해 set 사용

    # 1. 모든 길이의 순열 생성
    for i in range(1, len(numbers)+1):
        for p in permutations(numbers, i):
            num = int(''.join(p))
            comb.add(num)
    
    # 2. 소수 판별 함수
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    
    # 3. 소수 개수 세기
    for c in comb:
        if is_prime(c):
            answer += 1

    return answer