def first_and_last_index(arr, number):
    """
    Given a sorted array that may have duplicate values, use binary 
    search to find the first and last indexes of a given value.

    Args:
        arr(list): Sorted array (or Python list) that may have duplicate values
        number(int): Value to search for in the array
    Returns:
        a list containing the first and last indexes of the given value
    """
    start, end = 0, len(arr) - 1
    index = -1
    
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < number:
            start = mid + 1
        elif arr[mid] > number:
            end = mid - 1
        else:
            index = mid
            break
    
    if index == -1:
        return [-1, -1]
    
    first, last = index, index
    
    while arr[first] == number:
        if first <= start:
            break
        if arr[first - 1] == number:
            first -= 1
        else:
            break
            
    while arr[last] == number:
        if last >= end:
            break
        if arr[last + 1] == number:
            last += 1
        else:
            break
            
    return [first, last]


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    solution = test_case[2]
    output = first_and_last_index(input_list, number)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

input_list = [1]
number = 1
solution = [0, 0]
test_case_1 = [input_list, number, solution]
test_function(test_case_1)

input_list = [0, 1, 2, 3, 3, 3, 3, 4, 5, 6]
number = 3
solution = [3, 6]
test_case_2 = [input_list, number, solution]
test_function(test_case_2)

input_list = [0, 1, 2, 3, 4, 5]
number = 5
solution = [5, 5]
test_case_3 = [input_list, number, solution]
test_function(test_case_3)

input_list = [0, 1, 2, 3, 4, 5]
number = 6
solution = [-1, -1]
test_case_4 = [input_list, number, solution]
test_function(test_case_4)