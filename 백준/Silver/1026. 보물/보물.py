N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A의 가장 큰 값과 B의 가장 작은 값을 곱해보자
A.sort()
B.sort(reverse=True)

S = 0

for i in range(len(A)):
    S += A[i]*B[i]

print(S)