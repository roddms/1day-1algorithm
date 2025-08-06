N = int(input())
narr = set(map(int, input().split()))

M = int(input())
marr = list(map(int, input().split()))

for m in marr:
    print(1 if m in narr else 0)
