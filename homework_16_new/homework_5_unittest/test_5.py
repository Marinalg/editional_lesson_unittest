import unittest
import homework_5

class Homework_five_test(unittest.TestCase):
    def test_positive(self):
        """return is str"""
        out = homework_5.homework()
        self.assertIsInstance(out, str)

    def test_positive_1(self):
        data_list = 'john marta james Morgan Adam Maria huang'
        out = homework_5.homework()
        self.assertIsInstance(out, data_list)



if __name__ == "__main__":
    unittest.main(verbosity=2)