def find_partition(arr):
    n = len(arr)
    total_sum = sum(arr)
    
    target = total_sum // 2
    
    # possible subset sizes
    sizes = []
    if n % 2 == 0:
        sizes = [n // 2]
    else:
        sizes = [n // 2, (n // 2) + 1]
    
    result = []
    
    def backtrack(start, k, curr_subset):
        if len(curr_subset) == k:
            if sum(curr_subset) == target:
                result.append(curr_subset[:])
                return True
            return False
        
        for i in range(start, n):
            curr_subset.append(arr[i])
            if backtrack(i + 1, k, curr_subset):
                return True
            curr_subset.pop()
        
        return False
    
    for k in sizes:
        if backtrack(0, k, []):
            subset1 = result[0]
            subset2 = arr[:]
            
            # remove subset1 elements from subset2
            for x in subset1:
                subset2.remove(x)
            
            return [subset1, subset2]
    
    return []


# Examples
print(find_partition([1, 2, 3, 4]))
# Output: [[1, 4], [2, 3]]

print(find_partition([5, 10, 15]))
# Output: [[5, 10], [15]]
