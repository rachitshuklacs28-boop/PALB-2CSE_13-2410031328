def min_people(arr):
    n = len(arr)
    
    # Step 1: Build intervals
    intervals = []
    for i in range(n):
        if arr[i] != -1:
            left = max(0, i - arr[i])
            right = min(n - 1, i + arr[i])
            intervals.append((left, right))
    
    # Step 2: Sort intervals by start
    intervals.sort()
    
    # Step 3: Greedy covering
    count = 0
    i = 0
    current_end = 0
    farthest = 0
    
    while current_end < n:
        found = False
        
        while i < len(intervals) and intervals[i][0] <= current_end:
            farthest = max(farthest, intervals[i][1])
            i += 1
            found = True
        
        if not found:
            return -1
        
        count += 1
        current_end = farthest + 1
    
    return count