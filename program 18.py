def isSubset(a, b):
    freq = {}
    for num in a:
        freq[num] = freq.get(num, 0) + 1
    for num in b:
        if num not in freq or freq[num] == 0:
            return False
        freq[num] -= 1
    
    return True
print(isSubset([11,7,1,13,21,3,7,3], [11,3,7,1,7]))  
print(isSubset([1,2,3,4,4,5,6], [1,2,4]))            
print(isSubset([10,5,2,23,19], [19,5,3]))            