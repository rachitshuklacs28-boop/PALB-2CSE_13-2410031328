def minJumps(arr):
    n = len(arr)
    if n <= 1:
        return 0
    if arr[0] == 0:
        return -1
    
    jumps = 0
    current_end = 0
    farthest = 0
    
    for i in range(n - 1):
        farthest = max(farthest, i + arr[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
            if current_end >= n - 1:
                return jumps
        if i >= farthest:
            return -1
    
    return -1

print(minJumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))  
print(minJumps([1, 4, 3, 2, 6, 7]))                
print(minJumps([0, 10, 20]))                       