def chocolate_distribution(arr, m):
    n = len(arr)
    
    if m == 0 or n == 0:
        return 0
    
    if m > n:
        return -1   

    arr.sort()

    min_diff = float('inf')

    for i in range(n - m + 1):
        diff = arr[i + m - 1] - arr[i]
        if diff < min_diff:
            min_diff = diff
    
    return min_diff

print(chocolate_distribution([3, 4, 1, 9, 56, 7, 9, 12], 5))  
print(chocolate_distribution([7, 3, 2, 4, 9, 12, 56], 3))     
print(chocolate_distribution([3, 4, 1, 9, 56], 5))            