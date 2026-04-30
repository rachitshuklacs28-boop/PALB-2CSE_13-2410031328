def smallest_subarray(arr, x):
    n = len(arr)
    min_length = n + 1
    current_sum = 0
    start = 0

    for end in range(n):
        current_sum += arr[end]

        while current_sum > x:
            length = end - start + 1
            if length < min_length:
                min_length = length
            
            current_sum -= arr[start]
            start += 1

    if min_length == n + 1:
        return 0
    else:
        return min_length

print(smallest_subarray([1, 4, 45, 6, 0, 19], 51))  
print(smallest_subarray([1, 10, 5, 2, 7], 100))     