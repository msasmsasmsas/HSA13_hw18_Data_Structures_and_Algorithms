.\.venv\Scripts\Activate.ps1

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest tests/red_black_tree_test.py -v -s
pytest tests/red_black_tree_performance_test.py -v -s
pytest tests/counting_sort_test.py -v -s
pytest tests/counting_sort_performance_test.py -v -s
