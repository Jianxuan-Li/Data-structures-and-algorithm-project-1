def findMedian(arr):
    arr.sort()
    return arr[len(arr) // 2]

def split_list(arr, n):
    return [arr[i:i + n] for i in range(0, len(arr), n)]

def fastSelect(Arr, k):
    if k <= 0 or len(Arr) < 1:
        return None
    
    mids = []
    n = len(Arr)
    
    sub_arr = split_list(Arr, 5)
                                    
    for i in range(len(sub_arr)):
        mids.append(findMedian(sub_arr[i]))
    
    if len(mids) == 1:
        pivot = mids[0]
    elif len(mids) > 1:
        pivot = fastSelect(mids, (len(mids) // 2))
        
    Arr_Less_P = []
    Arr_Equal_P = []
    Arr_More_P = []

    # Step 4 - Partition the original Arr into three sub-arrays
    for element in Arr:
        if (element<pivot):
            Arr_Less_P.append(element)
        elif (element>pivot):
            Arr_More_P.append(element)
        else:
            Arr_Equal_P.append(element)

    # Step 5 - Recurse based on the sizes of the three sub-arrays
    if (k <= len(Arr_Less_P)):
        return fastSelect(Arr_Less_P, k)

    elif (k > (len(Arr_Less_P) + len(Arr_Equal_P))):
        return fastSelect(Arr_More_P, (k - len(Arr_Less_P) - len(Arr_Equal_P)))

    else:
        return pivot
        
    
Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42]
k = 5
print(fastSelect(Arr, k))        # Outputs 12

Arr = [5, 2, 20, 17, 11, 13, 8, 9, 11]
k = 5
print(fastSelect(Arr, k))        # Outputs 11

Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42, 99]
k = 10
print(fastSelect(Arr, k))        # Outputs 99