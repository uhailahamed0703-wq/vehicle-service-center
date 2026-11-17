def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []

    for element in arr[1:]:
        if element < pivot:
            left.append(element)
        else:
            right.append(element)

    return quick_sort(left) + [pivot] + quick_sort(right)


# Example usage of Quick Sort
arr = [12, 4, 5, 6, 7, 3, 1, 15]

sorted_arr = quick_sort(arr)

print("Array before sorting:", arr)
print("Array after sorting:", sorted_arr)