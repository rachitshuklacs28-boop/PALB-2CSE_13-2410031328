def three_way_partition(arr, a, b):
    n = len(arr)
    
    low = 0
    mid = 0
    high = n - 1
    
    while mid <= high:
        if arr[mid] < a:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
            
        elif a <= arr[mid] <= b:
            mid += 1
            
        else: 
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    
    return True

arr1 = [1, 2, 3, 3, 4]
print(three_way_partition(arr1, 1, 2), arr1)

arr2 = [1, 4, 3, 6, 2, 1]
print(three_way_partition(arr2, 1, 3), arr2)