def find_max(numbers):
    max_num = float('-inf')
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# Example usage
numbers = [5, 2, 9, 1, 7]
max_number = find_max(numbers)
print("The maximum number is:", max_number)