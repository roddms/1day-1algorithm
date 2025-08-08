N = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

left = 0
right = N - 1
min_sum = int(1e15)
min_a = 0
min_b = 0

while left < right:
    cur_sum = liquid[left] + liquid[right]

    if abs(cur_sum) < min_sum:
        min_sum = abs(cur_sum)
        min_a = liquid[left]
        min_b = liquid[right]

    if cur_sum < 0:
        left += 1
    else:
        right -= 1

print(min_a, min_b)
