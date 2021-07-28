import sys
sys.path.append('../')


import pytest

from CasinoBackEnd import SQL_Database
import unittest

class TestCases(unittest.TestCase):

    def testCase1(self, exp):
        expected = [] #correct result
        actual = [] #derived result
        self.assertEqual(expected, actual)