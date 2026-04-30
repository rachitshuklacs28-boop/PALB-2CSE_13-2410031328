import bisect

def row_with_max_ones(arr):
    n = len(arr)
    m = len(arr[0])
    
    max_ones = 0
    index = -1
    
    for i in range(n):
        first_one = bisect.bisect_left(arr[i], 1)
        
        ones_count = m - first_one
        
        if ones_count > max_ones:
            max_ones = ones_count
            index = i
    
    return index
print(row_with_max_ones([[0,1,1,1],
                         [0,0,1,1],
                         [1,1,1,1],
                         [0,0,0,0]]))   

print(row_with_max_ones([[0,0],
                         [1,1]]))      

print(row_with_max_ones([[0,0],
                         [0,0]]))      