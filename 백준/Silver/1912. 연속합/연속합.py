n = int(input())
arr = list(map(int, input().split()))

prefix = [0] * n  # 정답 길이만큼 정확히 만듦
prefix[0] = arr[0]  # 첫 값은 그대로 시작

for i in range(1, n):
    prefix[i] = max(prefix[i - 1] + arr[i], arr[i])  # 핵심 로직

print(max(prefix))