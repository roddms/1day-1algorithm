N = int(input())
info = list(map(int, input().split()))
ans = [0] * N

# 키 작은 순서부터 채우기
# 왼쪽에 키 큰 사람 수 만큼 넘어가기
for i in range(N):
    cnt = 0

    for j in range(N):
        if cnt == info[i] and ans[j] == 0:
            ans[j] = i + 1
            break

        elif ans[j] == 0:
            cnt += 1
        

print(*ans)