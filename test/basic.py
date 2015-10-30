
import unittest

class GitTocBasicTestCase(unittest.TestCase):
    """ Basic true asserts to see that testing is executed
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_example(self):
        self.assertEqual(True, True)
        self.assertNotEqual(True, False)

if __name__ == '__main__':
    unittest.main()
