def combination_sum2(candidates, target):
    result = []
    candidates.sort()  
    
    def backtrack(start, current, total):
        if total == target:
            result.append(current[:])
            return
        
        if total > target:
            return
        
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            
            current.append(candidates[i])
            backtrack(i + 1, current, total + candidates[i]) 
            current.pop()
    
    backtrack(0, [], 0)
    return result
print(combination_sum2([10,1,2,7,6,1,5], 8))

print(combination_sum2([2,5,2,1,2], 5))
