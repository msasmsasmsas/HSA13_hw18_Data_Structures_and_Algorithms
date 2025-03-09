import time
import random
import matplotlib.pyplot as plt
from red_black_tree.red_black_tree import RedBlackTree


def measure_time(func, *args):
    """Helper function to measure execution time of a function."""
    start_time = time.time()
    func(*args)
    return time.time() - start_time


def test_red_black_tree_performance():
    """Measures the performance of insert, search, and delete operations."""

    sizes = [100000, 200000, 400000, 600000, 800000]  # Different dataset sizes
    insert_times = []
    search_times = []
    delete_times = []

    for size in sizes:
        curr_insert_times = []
        curr_search_times = []
        curr_delete_times = []
        for _ in range(0, 3):
            rbt = RedBlackTree()
            data = random.sample(range(1, size * 10), size)  # Generate unique random numbers

            insert_time = measure_time(lambda: [rbt.insert(num) for num in random.sample(data, size)])
            curr_insert_times.append(insert_time)

            search_time = measure_time(lambda: [rbt.find(num) for num in random.sample(data, size)])
            curr_search_times.append(search_time)

            delete_time = measure_time(lambda: [rbt.find(num) for num in random.sample(data, size)])
            curr_delete_times.append(delete_time)

        insert_times.append((sum(curr_insert_times) / len(curr_insert_times)))
        search_times.append((sum(curr_search_times) / len(curr_search_times)))
        delete_times.append((sum(curr_delete_times) / len(curr_delete_times)))

        print(f"Size: {size} | Insert: {insert_time:.4f}s | Search: {search_time:.4f}s | Delete: {delete_time:.4f}s")

    plt.figure(figsize=(10, 5))
    plt.plot(sizes, insert_times, label="Insert Time", marker="o")
    plt.plot(sizes, search_times, label="Search Time", marker="s")
    plt.plot(sizes, delete_times, label="Delete Time", marker="^")

    plt.xlabel("Number of Elements")
    plt.ylabel("Time (seconds)")
    # plt.xscale("log")
    # plt.yscale("log")
    plt.title("Red-Black Tree Performance")
    plt.legend()
    plt.grid()
    plt.savefig("rbt_performance.png")
    plt.show(block=True)


test_red_black_tree_performance()