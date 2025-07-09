# 임수 수행 일수, 최소 기여도
N, M = map(int, input().split())

# 정보 수집 입무 진척도
info = list(map(int,input().split()))

# 감시 임무 진척도
see = list(map(int,input().split()))

mission = info + see # info랑 see를 1차원 리스트로 합치기

ans = 0

def recur(day, cur_sum, prev_location):
    global mission, ans

    if day == N+1:
        if cur_sum >= M:
            ans += 1
        return
    
    # 6개 미션 모두 돌며 경우의 수 계산
    for i in range(6):
        cur_location = i % 3
        today_progress = mission[i]

        # 장소 이전과 같으면 진척도 절반
        if cur_location == prev_location:
            today_progress = today_progress//2

        # 다음날, 진척도 추가, 현재 위치
        recur(day +1, cur_sum + today_progress, cur_location)


recur(1, 0, -1)

print(ans)
        


