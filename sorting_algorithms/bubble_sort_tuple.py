# Entries are (h, m) where h is the hour and m is the minute
sleep_times = [(24,13), (21,55), (23,20), (22,5), (24,23), (21,58), (24,3)]

def bubble_sort(arr: list) -> list:
    for i in range(len(arr)):
        for j in range(1, len(arr)):
            this = arr[j]
            prev = arr[j - 1]
            
            if this[0] < prev[0] or (this[0] == prev[0] and this[1] < prev[1]):
                arr[j], arr[j-1] = prev, this
            
    return arr

print(sleep_times)
print(bubble_sort(sleep_times))