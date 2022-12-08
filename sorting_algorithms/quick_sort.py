def sort_a_part(items, start_index, end_index):
    # select the last element as the pivot
    pivot_index = end_index
    left_index = start_index

    while pivot_index != left_index:
        item = items[left_index]

        if item < items[pivot_index]:
            left_index += 1
            continue

        items[left_index] = items[pivot_index - 1]
        items[pivot_index - 1] = items[pivot_index]
        items[pivot_index] = item
        pivot_index -= 1
    
    return pivot_index
        
def sort_all(items, begin_index, end_index):
    if begin_index > end_index:
        return
    
    pivot_index = sort_a_part(items, begin_index, end_index)
    sort_all(items, begin_index, pivot_index - 1)
    sort_all(items, pivot_index + 1, end_index)
    
def quicksort(items):
    sort_all(items, 0, len(items) - 1)
    
items = [8, 3, 1, 7, 0, 10, 2]
quicksort(items)
print(items)