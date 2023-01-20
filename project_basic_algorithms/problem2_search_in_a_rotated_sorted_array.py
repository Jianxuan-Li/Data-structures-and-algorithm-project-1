def helper(input_list, number, start, end):
    if start == end and input_list[start] == number:
        return start
    
    if start == end and input_list[start] != number:
        return -1
    
    mid = (start + end) // 2

    left = helper(input_list, number, start, mid)
    if left != -1:
        return left
    
    right = helper(input_list, number, mid + 1, end)
    if right != -1:
        return right
    
    return -1
    
def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    index = helper(input_list, number, 0, len(input_list) - 1)
    return index
   

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])