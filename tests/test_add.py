import unittest
from add import add


class TestAdd(unittest.TestCase):

    def test_add_return_sum_of_two_value(self):
        result = add(1, 2)
        self.assertEqual(result, 3)
