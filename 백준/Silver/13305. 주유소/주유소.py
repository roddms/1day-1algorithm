N = int(input())
dist = list(map(int,input().split())) # N-1개
price = list(map(int,input().split()))  # N개

min_price = price[0]
ans = 0

for i in range(N-1):
    if price[i] < min_price:
        min_price = price[i]

    ans += dist[i] * min_price

print(ans)