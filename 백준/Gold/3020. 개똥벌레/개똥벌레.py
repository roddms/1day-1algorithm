# 이분 탐색
# 종유석과 석순을 각각 구하고
# 각 높이별로 부딪히는 장애물의 합을 구해서 res에 append
# print(min(res), cnt)

import sys 
input = sys.stdin.readline

N, H = map(int, input().split()) # 동굴의 길이와 높이

top = [] # 종유석 -> top의 값보다 크면 부딪힘
bottom = [] # 석순 -> bot의 값보다 작으면 부딪힘

for i in range(N):
    if i%2 == 0: # 석순
        bottom.append(int(input()))

    else: # 종유석
        top.append(int(input()))

top.sort()
bottom.sort()

def binary_search(arr, num):
    cur = -1
    step = len(arr)

    while step != 0:
        while cur + step < len(arr) and arr[cur + step] <= num:
            cur += step
        step //= 2
		
    return cur

res = [0] * (H + 1)  # 높이별 충돌 수

min_crash = N + 1
count = 0

for h in range(1, H + 1):
    # 석순 중 길이가 h 이상인 개수 → 전체 - (h-1 이하 개수)
    b = len(bottom) - (binary_search(bottom, h - 1) + 1)

    # 종유석 중 길이가 H - h + 1 이상인 개수
    t = len(top) - (binary_search(top, H - h) + 1)

    crash = b + t
    res[h] = crash

    if crash < min_crash:
        min_crash = crash
        count = 1
    elif crash == min_crash:
        count += 1

print(min_crash, count)
  