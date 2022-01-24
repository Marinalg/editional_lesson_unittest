import unittest
from homework_9 import arithmetic
import os
from logger import log


class HomeworkWork9Test(unittest .TestCase):
    def test_mult(self):
        a = 5
        b = 1
        c = 5
        out = arithmetic(a, b, "*")
        self.assertEqual(out, c)
        log.debug('result of homework' )

    @unittest.skip('its skip test')
    def test_mult_v2(self):
        from homework_9.1 import math as ar2
        a =7
        exp = 14
        out = ar2(a * math.sqrt(2))
        self.test_mult(out,exp)

    @unittest.skipIf( os.name == "posix", "Mac: Catalina is not support")
    def test_mult(self):
        a = 5
        b = 1
        c = 5
        out = arithmetic(a, b, "*")
        self.assertEqual(out, c)


if __name__ == "__main__" :
    unittest.main(verbosity=2)



