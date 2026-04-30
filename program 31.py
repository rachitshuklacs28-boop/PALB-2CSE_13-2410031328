def combination_sum(candidates, target):
    result = []
    
    def backtrack(start, current, total):
        if total == target:
            result.append(current[:])
            return
        if total > target:
            return
        for i in range(start, len(candidates)):
            current.append(candidates[i])
            backtrack(i, current, total + candidates[i])  
            current.pop()  
    
    backtrack(0, [], 0)
    return result

print(combination_sum([2,3,6,7], 7))  


print(combination_sum([2,3,5], 8))  


print(combination_sum([2], 1))  
