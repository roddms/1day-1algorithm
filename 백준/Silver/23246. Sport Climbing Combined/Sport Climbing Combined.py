n = int(input())
score = []

# 1. 곱한 순위 낮은 경우 우선
# 2. 합산 순위 낮은 경우 우선
# 3. 등번호 낮은 경우 우선

for _ in range(n):
    b, p, q, r = map(int, input().split())
    score.append((b, p, q, r))

# 정렬: key = (곱, 합, 등번호)
score.sort(key=lambda x: (x[1]*x[2]*x[3], x[1]+x[2]+x[3], x[0]))

for i in range(3):
    print(score[i][0], end=' ')