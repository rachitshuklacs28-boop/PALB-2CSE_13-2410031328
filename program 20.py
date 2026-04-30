def trap(arr):
    n = len(arr)
    
    left = 0
    right = n - 1
    left_max = 0
    right_max = 0
    water = 0
    
    while left <= right:
        
        if arr[left] < arr[right]:
            
            if arr[left] >= left_max:
                left_max = arr[left]
            else:
                water += left_max - arr[left]
            
            left += 1
        
        else:
            
            if arr[right] >= right_max:
                right_max = arr[right]
            else:
                water += right_max - arr[right]
            
            right -= 1
    
    return water
print(trap([3,0,1,0,4,0,2]))   
print(trap([3,0,2,0,4]))       
print(trap([1,2,3,4]))         
print(trap([2,1,5,3,1,0,4]))   