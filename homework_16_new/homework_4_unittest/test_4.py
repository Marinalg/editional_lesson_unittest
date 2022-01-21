import unittest
import homework_4

class Homework_four_test(unittest.TestCase):
    def test_positive(self):
        """test out the value"""
        out = homework_4.print_escape_table(r'\a', 'Bell (alert)')
        exp = "|\t|\a    | a |"
        self.assertEqual(out, exp)


if __name__ == "__main__":
    unittest.main(verbosity=2)

