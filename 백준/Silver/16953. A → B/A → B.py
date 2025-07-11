A, B = map(int, input().split())
cnt = 0

while A < B:

    if B % 2 == 0:
        B //= 2

    elif B % 10 == 1:
        B //= 10

    else: break

    cnt += 1

if A == B:
    print(cnt+1)
else:
    print(-1) 