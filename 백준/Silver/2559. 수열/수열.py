#2559

N, K = map(int, input().split())

tem = list(map(int,input().split()))

prefix = [0 for _ in range(N+1)]

for i in range(1, N+1):
    prefix[i] = prefix[i-1] + tem[i-1]

arr = []

for i in range(K, N+1):
    arr.append(prefix[i] - prefix[i-K])

print(max(arr))