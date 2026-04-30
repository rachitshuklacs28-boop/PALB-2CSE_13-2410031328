def previous_greater(arr):
    stack = []
    result = []
    
    for num in arr:
        # Remove elements <= current
        while stack and stack[-1] <= num:
            stack.pop()
        
        # If stack empty → no greater element
        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])
        
        # Push current element
        stack.append(num)
    
    return result


# Examples
print(previous_greater([10, 4, 2, 20, 40, 12, 30]))
# Output: [-1, 10, 4, -1, -1, 40, 40]

print(previous_greater([10, 20, 30, 40]))
# Output: [-1, -1, -1, -1]
