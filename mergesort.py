def merge_sort(arr):
    
    # Base case
    if len(arr) <= 1:
        return arr

    # Find the middle
    middle = len(arr) // 2

    # Divide into two halves
    left_half = arr[:middle]
    right_half = arr[middle:]

    # Sort the left half
    left_half = merge_sort(left_half)

    # Sort the right half
    right_half = merge_sort(right_half)

    # Merge both sorted halves
    result = merge(left_half, right_half)

    return result


def merge(left, right):

    result = []

    left_index = 0
    right_index = 0

    # Compare elements from left and right
    while left_index < len(left) and right_index < len(right):

        if left[left_index] < right[right_index]:

            result.append(left[left_index])
            left_index = left_index + 1

        else:

            result.append(right[right_index])
            right_index = right_index + 1

    # Add remaining elements from left
    while left_index < len(left):

        result.append(left[left_index])
        left_index = left_index + 1

    # Add remaining elements from right
    while right_index < len(right):

        result.append(right[right_index])
        right_index = right_index + 1

    return result


# Example
numbers = [38, 12, 27, 43, 9, 31, 18, 25]

# Call merge sort
sorted_numbers = merge_sort(numbers)

# Display result
print("Original:", numbers)
print("Sorted:", sorted_numbers)