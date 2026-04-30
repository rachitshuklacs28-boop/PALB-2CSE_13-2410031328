def count_valid_subarrays(arr):
    n = len(arr)
    stack = []
    nse = [n] * n   # default: no smaller element → n
    
    # Step 1: Find Next Smaller Element index
    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            idx = stack.pop()
            nse[idx] = i
        stack.append(i)
    
    # Step 2: Count subarrays
    count = 0
    for i in range(n):
        count += (nse[i] - i)
    
    return count


# Examples
print(count_valid_subarrays([1, 2, 1]))   # Output: 5
print(count_valid_subarrays([1, 3, 5, 2])) # Output: 8
