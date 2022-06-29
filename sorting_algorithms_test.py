# Unit testing file for the sorting_algorithms.py file

from cgi import test
import unittest
import random
import sorting_algorithms as sa

class TestListGen(unittest.TestCase):
    """
    Tests generation of random list using rand_array function in sorting_algorithms.py
    """
    def test_array_size(self):
        size = random.randint(1, 50)
        test_list = sa.rand_array(size)
        self.assertEqual(size, len(test_list))

class TestBubbleSort(unittest.TestCase):
    """
    Tests that bubble sort method properly sorts an input list
    """
    def test_bubble_sort(self):
        test_list = sa.rand_array(25)
        sorted_list = test_list
        sorted_list.sort()
        sa.bubble_sort(test_list)
        self.assertEqual(sorted_list, test_list)

if __name__ == "__main__":
    unittest.main()