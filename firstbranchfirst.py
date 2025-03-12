def find_max_element(lst):
    max_element = lst[0]
    for element in lst:
        if element > max_element:
            max_element = element
    return max_element

# Example usage
my_list = [5, 2, 9, 1, 7]
max_value = find_max_element(my_list)
print("The maximum element is:", max_value)