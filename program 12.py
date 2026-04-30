def getMinDiff(arr, k):
    n = len(arr)
    
    arr.sort()
    ans = arr[n-1] - arr[0]
    
    smallest = arr[0] + k
    largest = arr[n-1] - k
    
    for i in range(n-1):
        
        if arr[i+1] - k < 0:
            continue
        
        min_height = min(smallest, arr[i+1] - k)
        max_height = max(largest, arr[i] + k)
        
        ans = min(ans, max_height - min_height)
    
    return ans
arr1 = [1, 5, 8, 10]
k1 = 2
print(getMinDiff(arr1, k1))   

arr2 = [3, 9, 12, 16, 20]
k2 = 3
print(getMinDiff(arr2, k2))  