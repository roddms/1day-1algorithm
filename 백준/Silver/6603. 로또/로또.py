def combination(index, level):
    global k, S, choose

    if level == 6:
        for c in choose:
            print(c, end= ' ')
        print()
        return
    
    for i in range(index, k):
        choose.append(S[i])
        combination(i+1, level+1)
        choose.pop()

while True:
    choose = []
    I = list(map(int, input().split()))

    k = I[0]
    S = I[1:]

    if k == 0:
        break

    combination(0,0)
    print()