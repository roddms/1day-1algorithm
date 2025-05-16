N = int(input())

for _ in range(N):
    S = int(input())
    
    if S == 1:
        print("NO")
        continue

    is_prime = True

    for i in range(2, 1000001):
        if S % i == 0:
            is_prime = False
            break

    print("YES" if is_prime else "NO")