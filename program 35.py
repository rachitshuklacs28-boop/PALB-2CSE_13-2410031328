def plus_one(digits):
    n = len(digits)
    for i in range(n - 1, -1, -1):
        
        if digits[i] < 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0

    return [1] + digits

print(plus_one([1,2,3]))   
print(plus_one([4,3,2,1])) 
print(plus_one([9]))       