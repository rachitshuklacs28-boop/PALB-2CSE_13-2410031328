def findLargest(arr):
    
    for num in arr:
        if num > largest:
            largest = num
            
    return largest

arr = [1, 8, 7, 56, 90]
result = findLargest(arr)
print(result)