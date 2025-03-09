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
pytest tests/red_black_tree_test_performance.py -v -s
pytest tests/counting_sort_test.py -v -s
pytest tests/counting_sort_test_performance.py -v -s
```

red-black-tree performance
Figure out when Counting Sort doesn’t perform

Counting sort is memory-inefficient when difference between min and max value (K) is much larger than number of elements (N)

red-black-tree performance
