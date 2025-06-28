N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
check = [False] * N
choose = []
used = set()

def permutation(level):
    if level == M:
        tup = tuple(choose)
        if tup not in used:
            used.add(tup)
            for t in tup:
                print(t, end=' ')
            print()
        return
    
    for i in range(N):
        if check[i] == True:
            continue

        choose.append(lst[i])
        check[i] = True

        permutation(level+1)

        check[i] = False
        choose.pop()


permutation(0)