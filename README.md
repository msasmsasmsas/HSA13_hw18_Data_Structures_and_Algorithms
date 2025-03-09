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
tests/counting_sort_test.py::test_counting_sort [2] -> [2]
[12, 3, 25, 30, 9] -> [3, 9, 12, 25, 30]
[32, 106, 69, 62, 172, 182, 97, 175, 29, 14, 124, 2, 30, 50, 57, 7, 139, 195, 103, 159] -> [2, 7, 14, 29, 30, 32, 50, 57, 62, 69, 97, 103, 106, 124, 139, 159, 172, 175, 182, 195]
[460, 495, 140, 311, 426, 255, 41, 344, 322, 210, 95, 347, 467, 130, 247, 315, 161, 280, 144, 48, 393, 155, 376, 349, 5, 235, 342, 374, 478, 299, 119, 381, 253, 241, 294, 373, 87, 378, 75,
 455, 196, 85, 461, 423, 339, 433, 12, 343, 25, 131] -> [5, 12, 25, 41, 48, 75, 85, 87, 95, 119, 130, 131, 140, 144, 155, 161, 196, 210, 235, 241, 247, 253, 255, 280, 294, 299, 311, 315, 322, 339, 342, 343, 344, 347, 349, 373, 374, 376, 378, 381, 393, 423, 426, 433, 455, 460, 461, 467, 478, 495]
[862, 988, 417, 192, 46, 153, 712, 26, 799, 852, 262, 970, 925, 963, 726, 584, 568, 61, 951, 95, 197, 282, 593, 4, 849, 406, 934, 164, 119, 717, 207, 308, 552, 182, 647, 425, 853, 372, 766
, 356, 465, 525, 534, 206, 336, 674, 589, 346, 463, 514, 38, 334, 622, 641, 611, 303, 220, 385, 309, 212, 709, 783, 661, 767, 950, 260, 723, 402, 690, 167, 633, 412, 631, 800, 840, 698, 45
2, 702, 287, 132, 859, 879, 637, 656, 234, 377, 330, 398, 124, 141, 541, 557, 778, 651, 460, 173, 520, 67, 470, 874] -> [4, 26, 38, 46, 61, 67, 95, 119, 124, 132, 141, 153, 164, 167, 173, 
182, 192, 197, 206, 207, 212, 220, 234, 260, 262, 282, 287, 303, 308, 309, 330, 334, 336, 346, 356, 372, 377, 385, 398, 402, 406, 412, 417, 425, 452, 460, 463, 465, 470, 514, 520, 525, 534
, 541, 552, 557, 568, 584, 589, 593, 611, 622, 631, 633, 637, 641, 647, 651, 656, 661, 674, 690, 698, 702, 709, 712, 717, 723, 726, 766, 767, 778, 783, 799, 800, 840, 849, 852, 853, 859, 862, 874, 879, 925, 934, 950, 951, 963, 970, 988]
[1717, 172, 1860, 1127, 154, 758, 1899, 366, 1670, 63, 1197, 1083, 129, 1796, 408, 851, 501, 1051, 690, 747, 1102, 1609, 144, 694, 1654, 350, 740, 1418, 447, 372, 1822, 438, 1719, 867, 956
, 276, 1470, 1526, 1499, 95, 1340, 1825, 1106, 1489, 892, 68, 869, 1259, 1808, 1932, 1977, 777, 1376, 1606, 1753, 1437, 142, 113, 1560, 861, 982, 368, 1864, 902, 1681, 1677, 1934, 618, 188
9, 781, 1841, 1323, 1862, 133, 1924, 414, 797, 1806, 1767, 1215, 993, 405, 1236, 266, 653, 1601, 1940, 1027, 1025, 41, 942, 1858, 1852, 1417, 1725, 642, 1049, 363, 1176, 348, 1319, 1044, 1
794, 732, 973, 444, 349, 1125, 81, 1192, 1389, 1420, 155, 1549, 16, 1312, 977, 224, 1204, 1839, 1174, 1751, 140, 891, 1009, 1440, 1239, 724, 1836, 1611, 744, 1555, 1327, 492, 1637, 769, 11
88, 311, 1149, 1715, 1022, 1460, 1104, 904, 145, 1542, 269, 253, 1919, 101, 64, 1518, 749, 1381, 482, 1798, 949, 138, 1446, 945, 998, 100, 1181, 247, 1344, 1128, 354, 383, 1298, 1288, 396,
 808, 976, 1978, 734, 24, 1430, 598, 1353, 1266, 1198, 1070, 1269, 272, 429, 1071, 1896, 676, 416, 1282, 1830, 1955, 518, 46, 1700, 1879, 1213, 1195, 871, 441] -> [16, 24, 41, 46, 63, 64, 
68, 81, 95, 100, 101, 113, 129, 133, 138, 140, 142, 144, 145, 154, 155, 172, 224, 247, 253, 266, 269, 272, 276, 311, 348, 349, 350, 354, 363, 366, 368, 372, 383, 396, 405, 408, 414, 416, 4
29, 438, 441, 444, 447, 482, 492, 501, 518, 598, 618, 642, 653, 676, 690, 694, 724, 732, 734, 740, 744, 747, 749, 758, 769, 777, 781, 797, 808, 851, 861, 867, 869, 871, 891, 892, 902, 904,
 942, 945, 949, 956, 973, 976, 977, 982, 993, 998, 1009, 1022, 1025, 1027, 1044, 1049, 1051, 1070, 1071, 1083, 1102, 1104, 1106, 1125, 1127, 1128, 1149, 1174, 1176, 1181, 1188, 1192, 1195,
 1197, 1198, 1204, 1213, 1215, 1236, 1239, 1259, 1266, 1269, 1282, 1288, 1298, 1312, 1319, 1323, 1327, 1340, 1344, 1353, 1376, 1381, 1389, 1417, 1418, 1420, 1430, 1437, 1440, 1446, 1460, 1
470, 1489, 1499, 1518, 1526, 1542, 1549, 1555, 1560, 1601, 1606, 1609, 1611, 1637, 1654, 1670, 1677, 1681, 1700, 1715, 1717, 1719, 1725, 1751, 1753, 1767, 1794, 1796, 1798, 1806, 1808, 1822, 1825, 1830, 1836, 1839, 1841, 1852, 1858, 1860, 1862, 1864, 1879, 1889, 1896, 1899, 1919, 1924, 1932, 1934, 1940, 1955, 1977, 1978]
PASSED



pytest tests/counting_sort_performance_test.py -v -s
```

red-black-tree performance
Figure out when Counting Sort doesn’t perform

Counting sort is memory-inefficient when difference between min and max value (K) is much larger than number of elements (N)

red-black-tree performance
