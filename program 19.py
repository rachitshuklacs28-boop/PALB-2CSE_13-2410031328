def findTriplet(arr, target):
    arr.sort()
    n = len(arr)
    
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        
        while left < right:
            total = arr[i] + arr[left] + arr[right]
            
            if total == target:
                return True
            elif total < target:
                left += 1
            else:
                right -= 1
    
    return False
print(findTriplet([1, 4, 45, 6, 10, 8], 13))  
print(findTriplet([1, 2, 4, 3, 6, 7], 10))    
print(findTriplet([40, 20, 10, 3, 6, 7], 24)) 
