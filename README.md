# HSA13_hw18_Data_Structures_and_Algorithms

mplement class for Balanced Binary Search Tree that can insert, find and delete elements.

Generate 100 random datasets and measure complexity.

Implement Counting Sort algorithm.

Figure out when Counting Sort doesn’t perform.

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest tests/red_black_tree-test.py -v -s

tests/red_black_tree_test.py::test_insertion PASSED
tests/red_black_tree_test.py::test_find PASSED
tests/red_black_tree_test.py::test_deletion PASSED



pytest tests/red_black_tree_performance_test.py -v -s

collecting ...
Size: 100000 | Insert: 0.4199s | Search: 0.2474s | Delete: 0.2353s
Size: 200000 | Insert: 0.9376s | Search: 0.5709s | Delete: 0.5643s
Size: 400000 | Insert: 2.7421s | Search: 1.5049s | Delete: 1.3954s
Size: 600000 | Insert: 4.8617s | Search: 2.2210s | Delete: 2.2496s
Size: 800000 | Insert: 7.3636s | Search: 3.5270s | Delete: 3.1477s
collected 1 item      



pytest tests/counting_sort_test.py -v -s
pytest tests/counting_sort_performance_test.py -v -s
```

red-black-tree performance
Figure out when Counting Sort doesn’t perform

Counting sort is memory-inefficient when difference between min and max value (K) is much larger than number of elements (N)

red-black-tree performance
