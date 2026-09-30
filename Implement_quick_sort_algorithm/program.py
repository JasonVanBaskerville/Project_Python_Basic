def quick_sort(array: list[int]) -> list[int]:
    if len(array) <= 1:
        return array
    pivot = array[0]
    left_part = []
    right_part = []

    i = 1
    while i < len(array):
        if array[i] <= pivot:
            left_part.append(array[i])
        else:
            right_part.append(array[i])
        i += 1
    
    left_sorted = quick_sort(left_part)
    right_sorted = quick_sort(right_part)

    sorted_array = left_sorted + [pivot] + right_sorted

    return sorted_array

# quick_sort([20, 3, 14, 1, 5]) should return [1, 3, 5, 14, 20].
print(quick_sort([20, 3, 14, 1, 5]))

    