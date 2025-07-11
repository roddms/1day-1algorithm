N, M = map(int, input().split())
position = list(map(int, input().split()))
ans = 0

# 음, 양 따로 처리
neg = []
pos = []

for x in position:
    if x > 0:
        pos.append(x)
    else:
        neg.append(-x)

# 각각을 내림차순 정렬
neg.sort(reverse=True)
pos.sort(reverse=True)

# 양수에서 방문할 좌표
dist_p = []

# 음수에서 방문할 좌표
dist_n = []

for p in pos[::M]:
    dist_p.append(p)

for n in neg[::M]:
    dist_n.append(n)

if neg and pos:
    if max(neg) > max(pos):
        for d in dist_p:
            ans += 2*d

        for d in dist_n:
            ans += 2*d
            
        ans -= max(neg)
        print(ans)

    if max(pos) > max(neg):
        for d in dist_n:
            ans += 2*d

        for d in dist_p:
            ans += 2*d
            
        ans -= max(pos)
        print(ans)

elif pos:
    for d in dist_p:
            ans += 2*d
            
    ans -= max(pos)
    print(ans)

else :
    for d in dist_n:
            ans += 2*d
            
    ans -= max(neg)
    print(ans)
