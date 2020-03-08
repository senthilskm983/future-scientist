import unittest

from unittest.mock import patch


from .. import using_function


class TestAverage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Global Setup')

    @classmethod
    def tearDownClass(cls):
        print('Global teardown')

    def setUp(self):
        print('Setup')

    def tearDown(self):
        print('teardown')

    @patch('using_function.functools.reduce')
    def test_average_valid(self):
        """
        test valid scenarios
        """
        # mock_reduce.side_effect = ValueError
        out = using_function.average([10, 10, 10])
        self.assertFalse(out, False)


if __name__ == '__main__':
    unittest.main()
