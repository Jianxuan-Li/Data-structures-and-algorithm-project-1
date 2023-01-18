def maxSubArray(arr):
    '''
    param: An array `arr`
    return: The maximum sum of the contiguous subarray. 
    No need to return the subarray itself.
    '''
    return maxSubArrayRecursive(arr, 0, len(arr) - 1)
   
def maxSubArrayRecursive(arr, start, stop):
    if start == stop:
        return arr[start]
    
    if stop > start:
        mid = (stop + start) // 2
        left_sum = maxSubArrayRecursive(arr, start, mid)
        right_sum = maxSubArrayRecursive(arr, mid + 1, stop)
        crossing_sum = maxCrossingSum(arr, start, mid, stop)
        return max(crossing_sum, max(left_sum, right_sum))
    
    else:
        return arr[start]
    
def maxCrossingSum(arr, start, mid, stop):
    left_sum = arr[mid]
    left_max = arr[mid]
    
    for i in range(mid - 1, start - 1, -1):
        left_sum += arr[i]
        left_max = max(left_max, left_sum)
        
    right_sum = arr[mid + 1]
    right_max = arr[mid + 1]
    
    for i in range(mid + 2, stop + 1):
        right_sum += arr[i]
        right_max = max(right_max, right_sum)
        
    return left_max + right_max
    

arr = [-2, 7, -6, 3, 1, -4, 5, 7] 
print("Maximum Sum = ",maxSubArray(arr))     # Outputs 13

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
print("Maximum Sum = ",maxSubArray(arr))     # Outputs 6

arr = [-4, 14, -6, 7] 
print("Maximum Sum = ",maxSubArray(arr))     # Outputs 15

arr = [-2, 1, -3, 5, 0, 3, 2, -5, 4]
print("Maximum Sum = ",maxSubArray(arr))     # Outputs 10

arr = [-2, -5, 6, -2, -3, 1, 5, -6]
print("Maximum Sum = ",maxSubArray(arr))     # Outputs 7