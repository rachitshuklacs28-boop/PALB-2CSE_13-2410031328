def count_less_equal(arr, x):
    count = 0
    for num in arr:
        if num <= x:
            count += 1
    return count


# Examples
print(count_less_equal([4, 5, 8, 1, 3], 6))      # Output: 4
print(count_less_equal([6, 10, 12, 15, 2, 4, 5], 14))  # Output: 6
