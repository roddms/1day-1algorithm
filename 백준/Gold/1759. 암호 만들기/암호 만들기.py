def combination(index, level):
    global L, C, choose, lst

    if level == L:
        mo = [c for c in choose if c in 'aeiou']
        ja = [c for c in choose if c not in 'aeiou']

        if len(mo)>=1 and len(ja)>=2:
            for c in choose:
                print(c, end='')
            print()
            return 
    
    for i in range(index, C):
        choose.append(lst[i])
        combination(i+1, level+1)
        choose.pop()
    

L, C = map(int, input().split())
lst = input().split()
lst.sort()

choose = []
combination(0, 0)