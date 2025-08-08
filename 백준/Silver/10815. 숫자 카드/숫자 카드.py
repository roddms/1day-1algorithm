N = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()

M = int(input())
arr2 = list(map(int, input().split()))

def binary_search(arr, num):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left+right) // 2

        if arr[mid] < num:
            left = mid + 1

        if arr[mid] > num:       
            right = mid -1

        if arr[mid] == num:
            return 1
        
    return 0

ans = []

for num in arr2:
    ans.append(binary_search(arr1, num))

print(*ans)