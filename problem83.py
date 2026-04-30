def can_place(arr, k, min_diff):
    count = 1   # pick first element
    last = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] - last >= min_diff:
            count += 1
            last = arr[i]
        if count >= k:
            return True
    
    return False


def max_min_difference(arr, k):
    arr.sort()
    
    low = 0
    high = arr[-1] - arr[0]
    ans = 0
    
    while low <= high:
        mid = (low + high) // 2
        
        if can_place(arr, k, mid):
            ans = mid
            low = mid + 1   # try bigger distance
        else:
            high = mid - 1
    
    return ans


# Examples
print(max_min_difference([2, 6, 2, 5], 3))  
# Output: 1

print(max_min_difference([1, 4, 9, 0, 2, 13, 3], 4))  
# Output: 4
