import time
import random
import matplotlib.pyplot as plt
from counting_sort.counting_sort import counting_sort


def measure_time(func, *args):
    """Helper function to measure execution time of a function."""
    start_time = time.time()
    func(*args)
    return time.time() - start_time


def test_counting_sort_performance():
    small_k = 10
    large_k = 100
    sizes = [10000, 50000, 200000, 500000, 1000000]  # Different dataset sizes
    sort_times_per_size = []
    sort_times_per_delta = []

    for size in sizes:
        curr_sort_times_fixed_k = []
        curr_sort_times_increased_k = []

        for _ in range(0, 2):
            data_fixed_k = random.sample(range(1, size * small_k), size)  # Generate unique random numbers
            data_increased_k = random.sample(range(1, size * large_k), size)

            sort_time_fixed_k = measure_time(lambda: counting_sort(random.sample(data_fixed_k, size)))
            sort_time_increased_k = measure_time(lambda: counting_sort(random.sample(data_increased_k, size)))

            curr_sort_times_fixed_k.append(sort_time_fixed_k)
            curr_sort_times_increased_k.append(sort_time_increased_k)

        sort_times_per_size.append((sum(curr_sort_times_fixed_k) / len(curr_sort_times_fixed_k)))
        sort_times_per_delta.append((sum(curr_sort_times_increased_k) / len(curr_sort_times_increased_k)))

    plt.figure(figsize=(10, 5))
    plt.plot(sizes, sort_times_per_size, label="Sort K=10", marker="o")
    plt.plot(sizes, sort_times_per_delta, label="Sort K=100", marker="^")

    plt.xlabel("Number of Elements (N)")
    plt.ylabel("Time (seconds)")
    plt.title("Counting Sort performance")
    plt.legend()
    plt.grid()
    plt.savefig("counting_sort_performance.png")
    plt.show(block=True)


test_counting_sort_performance()