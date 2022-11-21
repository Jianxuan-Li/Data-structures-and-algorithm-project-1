def bubble_sort(arr: list) -> list:
    for i in range(len(arr)):
        for j in range(1, len(arr)):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                
    return arr

items = [16,49,3,12,56,49,55,22,13,46,19,55,46,13,25,56,9,48,45]
print(items)
print(bubble_sort(items))

items = [3,2,1]
print(items)
print(bubble_sort(items))