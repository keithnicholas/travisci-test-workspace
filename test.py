import unittest
def fun(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 24)


if __name__ == '__main__':
    unittest.main(verbosity=2)