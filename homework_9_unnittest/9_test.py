import unittest
from homework_9 import arithmetic
from homework_9_1 import math as ar2
from logger import log
import os



class HomeworkWork9Test(unittest.TestCase):
    def test_mult(self):
        a = 5
        b = 1
        c = 5
        out = arithmetic(a, b, "*")
        self.assertEqual(out, c)
        log.info("result of homework positive test case :multiplication")

    def test_sum_negative(self):
        a = 0
        b = 5
        c = 1
        out = arithmetic(a, b, "-")
        self.assertEqual(out, c)
        log.error("result of homework negative test case: division")

    @unittest.skip('its skip test')
    def test_square(self):
        a = 7
        exp = ar2.sqrt(2)
        self.test_square(exp)

    @unittest.skipIf(os.name == "posix", "Mac: Catalina is not support")
    def test_mult(self):
        a = 5
        b = 1
        c = 7
        out = arithmetic(a, b, "*")
        self.assertEqual(out, c)





if __name__ == "__main__" :
    unittest.main(verbosity=2)



