def previous_smaller(arr):
    stack = []
    result = []
    
    for num in arr:
        # Remove elements >= current
        while stack and stack[-1] >= num:
            stack.pop()
        
        # If stack empty → no smaller element
        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])
        
        # Push current element
        stack.append(num)
    
    return result


# Examples
print(previous_smaller([1, 6, 2]))  
# Output: [-1, 1, 1]

print(previous_smaller([1, 5, 0, 3, 4, 5]))  
# Output: [-1, 1, -1, 0, 3, 4]
