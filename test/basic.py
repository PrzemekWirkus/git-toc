
import unittest
from gittoc import mangle_header


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

    def test_smoke_tests_header_depth(self):
        self.assertEqual(mangle_header("Description", 1), "* [Description](#description)")
        self.assertEqual(mangle_header("Description", 2), "  * [Description](#description)")
        self.assertEqual(mangle_header("Description", 3), "    * [Description](#description)")
        self.assertEqual(mangle_header("Description", 4), "      * [Description](#description)")

    def test_smoke_tests_labels(self):
        self.assertEqual(mangle_header("", 1), "* [](#)")
        self.assertEqual(mangle_header("a", 1), "* [a](#a)")
        self.assertEqual(mangle_header("A", 1), "* [A](#a)")
        self.assertEqual(mangle_header("Abcde", 1), "* [Abcde](#abcde)")
        self.assertEqual(mangle_header("Switch --version", 1), "* [Switch --version](#switch---version)")
        self.assertEqual(mangle_header("Introduction / Examples", 1), "* [Introduction / Examples](#introduction--examples)")
        self.assertEqual(mangle_header("Revision 3 - duration v0.0.1", 1), "* [Revision 3 - duration v0.0.1](#revision-3---duration-v001)")
        self.assertEqual(mangle_header("Retrospective in 3 [sec.]", 1), "* [Retrospective in 3 [sec.]](#retrospective-in-3-sec)")

    def test_headers_depth_1(self):
        self.assertEqual(
            mangle_header("Example 2 - digest directly from file", 1),
            "* [Example 2 - digest directly from file](#example-2---digest-directly-from-file)")

        self.assertEqual(
            mangle_header("Example 3 - pipe test.txt file content (as in example 2)", 1),
            "* [Example 3 - pipe test.txt file content (as in example 2)](#example-3---pipe-testtxt-file-content-as-in-example-2)")

        self.assertEqual(
            mangle_header("Switch --use-tids example", 1),
            "* [Switch --use-tids example](#switch---use-tids-example)")

    def test_headers_depth_2(self):
        self.assertEqual(
            mangle_header("Environment Pre-Check", 2),
            "  * [Environment Pre-Check](#environment-pre-check)")

if __name__ == '__main__':
    unittest.main()
