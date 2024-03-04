def insertion_sort(arr, left, right, key=lambda x: x):
    for i in range(left + 1, right + 1):
        key_item = key(arr[i])
        j = i - 1
        while j >= left and key(arr[j]) > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item



def merge(arr, left, mid, right):
    len_left = mid - left + 1
    len_right = right - mid

    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len_left and j < len_right:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < len_left:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len_right:
        arr[k] = right_arr[j]
        j += 1
        k += 1


def timsort(arr, key=lambda x: x):
    min_run = 32
    n = len(arr)

    for i in range(0, n, min_run):
        insertion_sort(arr, i, min((i + min_run - 1), n - 1))

    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = left + size - 1
            right = min((left + 2 * size - 1), (n - 1))
            merge(arr, left, mid, right)
        size *= 2

    return arr
