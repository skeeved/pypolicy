import pytest

class Test(object):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_example(self):
        """Example test, always returns True"""
        assert 1 == 1


if __name__ == '__main__':
    unittest.installHandler()
    unittest.main()
