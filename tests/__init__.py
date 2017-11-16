import unittest


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_example(self):
        """Example test, always returns True"""
        self.assertEqual(1, 1, msg='test_example')


if __name__ == '__main__':
    unittest.installHandler()
    unittest.main()
