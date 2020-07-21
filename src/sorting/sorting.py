def merge(a, b):
    merged = []

    i = 0
    j = 0

    # both i and j in their respective range
    while i < len(a) and j < len(b):
        # append the lesser element first
        if a[i] < b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1

    # append the rest of the elements once
    # either i or j are out of range
    while i < len(a):
        merged.append(a[i])
        i += 1
    while j < len(b):
        merged.append(b[j])
        j += 1

    return merged


def merge_sort(arr):
    # BASE CASE: an array of 1 or 0 elements,
    # which means that it is already sorted
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    # recursively call merge_sort on the
    # left and right halves of the array
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # then merge them
    return merge(left, right)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, a, b):
    i = 0
    j = 0
    k = 0

    # both i and j in their respective range
    while i < len(a) and j < len(b):
        # append the lesser element first
        if a[i] < b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1

    # append the rest of the elements once
    # either i or j are out of range
    while i < len(a):
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len(b):
        arr[k] = b[j]
        j += 1
        k += 1

    return arr


def merge_sort_in_place(arr):
    # BASE CASE: an array of 1 or 0 elements,
    # which means that it is already sorted
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    # recursively call merge_sort on the
    # left and right halves of the array
    left = merge_sort_in_place(arr[:mid])
    right = merge_sort_in_place(arr[mid:])

    # then merge them
    return merge_in_place(arr, left, right)
