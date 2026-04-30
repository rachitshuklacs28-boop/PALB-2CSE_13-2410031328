def combination_sum_k(n, k):
    result = []
    
    def backtrack(start, path, remaining):
        # Valid combination
        if len(path) == k and remaining == 0:
            result.append(path[:])
            return
        
        # Invalid cases
        if len(path) > k or remaining < 0:
            return
        
        for i in range(start, 10):  # numbers 1 to 9
            path.append(i)
            backtrack(i + 1, path, remaining - i)
            path.pop()
    
    backtrack(1, [], n)
    return result


# Examples
print(combination_sum_k(9, 3))
# Output: [[1, 2, 6], [1, 3, 5], [2, 3, 4]]

print(combination_sum_k(3, 3))
# Output: []
