import random

from counting_sort.counting_sort import counting_sort

def test_counting_sort():
    sizes = [1, 5, 20]

    for size in sizes:
        data = random.sample(range(1, size * 10), size)

        result = counting_sort(data)
        print(data, '->', result)

        assert result == sorted(data)