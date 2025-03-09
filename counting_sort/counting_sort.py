def counting_sort(arr):
    """Sorts an array using the Counting Sort algorithm."""
    if not arr:
        return []

    min_val = min(arr)
    max_val = max(arr)
    range_size = max_val - min_val + 1

    count = [0] * range_size

    for num in arr:
        count[num - min_val] += 1

    sorted_arr = []
    for i in range(range_size):
        sorted_arr.extend([i + min_val] * count[i])

    return sorted_arr