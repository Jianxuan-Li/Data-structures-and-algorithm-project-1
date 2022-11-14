def binary_search(array, target):
    '''Write a function that implements the binary search algorithm using iteration
   
    args:
      array: a sorted array of items of the same type
      target: the element you're searching for
   
    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    start, end = 0, len(array) - 1
    
    while start <= end:
        mid = (end - start) // 2 + start
        if array[mid] < target:
            start = mid + 1
        elif array[mid] > target:
            end = mid - 1
        else:
            return mid
        
    return -1
    
    
def test_function(test_case):
    answer = binary_search(test_case[0], test_case[1])
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
index = 6
test_case = [array, target, index]
test_function(test_case)

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
target = 11
index = 11
test_case = [array, target, index]
test_function(test_case)

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
target = 5
index = 5
test_case = [array, target, index]
test_function(test_case)

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
target = 1
index = 1
test_case = [array, target, index]
test_function(test_case)

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
target = 3
index = 3
test_case = [array, target, index]
test_function(test_case)